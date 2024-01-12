import tkinter as tk
import random


class SnakeGame:
    def __init__(self, root, width=400, height=400):
        self.root = root
        self.root.title("Snake Game")
        self.canvas = tk.Canvas(root, width=width, height=height, bg="black")
        self.canvas.pack()

        self.snake = [(100, 100), (90, 100), (80, 100)]
        self.direction = "Right"
        self.food = self.create_food()
        self.score = 0

        self.score_label = tk.Label(
            root,
            text=f"Score: {self.score}",
            font=("Helvetica", 12),
            fg="white",
            bg="black",
        )
        self.score_label.pack()

        self.root.bind("<KeyPress>", self.on_key_press)
        self.move()

    def create_food(self):
        x = random.randint(0, 39) * 10
        y = random.randint(0, 39) * 10
        return self.canvas.create_rectangle(x, y, x + 10, y + 10, fill="red")

    def move(self):
        head = self.snake[0]
        if self.direction == "Right":
            new_head = (head[0] + 10, head[1])
        elif self.direction == "Left":
            new_head = (head[0] - 10, head[1])
        elif self.direction == "Up":
            new_head = (head[0], head[1] - 10)
        elif self.direction == "Down":
            new_head = (head[0], head[1] + 10)

        self.snake.insert(0, new_head)
        self.canvas.coords(self.food, *self.create_food())

        if self.check_collision():
            self.game_over()
            return

        if new_head[0] == self.canvas.winfo_width():
            new_head = (0, new_head[1])
        elif new_head[0] < 0:
            new_head = (self.canvas.winfo_width() - 10, new_head[1])
        elif new_head[1] == self.canvas.winfo_height():
            new_head = (new_head[0], 0)
        elif new_head[1] < 0:
            new_head = (new_head[0], self.canvas.winfo_height() - 10)

        if new_head == self.canvas.coords(self.food):
            self.canvas.delete(self.food)
            self.food = self.create_food()
            self.score += 1
            self.update_score()

        else:
            tail = self.snake.pop()
            self.canvas.delete(self.snake_part)

        self.snake_part = self.canvas.create_rectangle(
            *new_head, new_head[0] + 10, new_head[1] + 10, fill="green"
        )
        self.root.after(100, self.move)

    def on_key_press(self, event):
        if event.keysym == "Right" and self.direction != "Left":
            self.direction = "Right"
        elif event.keysym == "Left" and self.direction != "Right":
            self.direction = "Left"
        elif event.keysym == "Up" and self.direction != "Down":
            self.direction = "Up"
        elif event.keysym == "Down" and self.direction != "Up":
            self.direction = "Down"

    def check_collision(self):
        head = self.canvas.coords(self.snake_part)
        for part in self.snake[1:]:
            if head == self.canvas.coords(part):
                return True
        return False

    def game_over(self):
        self.canvas.create_text(
            self.canvas.winfo_width() // 2,
            self.canvas.winfo_height() // 2,
            text="Game Over",
            fill="white",
            font=("Helvetica", 16, "bold"),
        )
        self.root.quit()

    def update_score(self):
        self.score_label.config(text=f"Score: {self.score}")


if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
