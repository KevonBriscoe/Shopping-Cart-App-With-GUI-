import json
import sys
from PyQt5.QtWidgets import QPushButton, QWidget, QLabel, QVBoxLayout, QLineEdit, QApplication, QTextEdit,QHBoxLayout


class shop_cart(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Shopping Cart")
        self.setGeometry(100, 100, 600, 600)

        self.item_label = QLabel("Enter your item:", self)
        self.item_input = QLineEdit(self)

        self.quantity_label = QLabel("Enter your quantity:", self)
        self.quantity_input = QLineEdit(self)

        self.price_label = QLabel("Enter your price:", self)
        self.price_input = QLineEdit(self)

        self.finish_label = QPushButton("Add", self)

        self.totalcost = QPushButton("Calculate Total", self)

        self.list = QTextEdit(self)
        self.list.setReadOnly(True)

        self.tot = QTextEdit(self)
        self.tot.setReadOnly(True)


        layout = QVBoxLayout()
        layout.addWidget(self.item_label)
        layout.addWidget(self.item_input)
        layout.addWidget(self.quantity_label)
        layout.addWidget(self.quantity_input)
        layout.addWidget(self.price_label)
        layout.addWidget(self.price_input)
        layout.addWidget(self.finish_label)
        layout.addWidget(self.totalcost)
        layout.addWidget(self.list)
        layout.addWidget(self.tot)
        self.setLayout(layout)

        self.finish_label.clicked.connect(self.shopping_cart)
        self.totalcost.clicked.connect(self.total)

        self.cart_list = []

    def shopping_cart(self):
            item = self.item_input.text()
            try:
                quantity = int(self.quantity_input.text())
                price = float(self.price_input.text())
            except ValueError:
                self.list.setText("Please enter a number")
                return
            self.cart_list.append({"item": item, "quantity": quantity, "price": price})
            self.item_input.clear()
            self.quantity_input.clear()
            self.price_input.clear()
            display = ""
            for exp in self.cart_list:
                display += f"Added {exp['quantity']} of {exp['item']} for ${exp['price']:.2f}\n"
            self.list.setText(display)
    def total(self):
        total = 0
        for item in self.cart_list:
            total += item["price"] * item["quantity"]
        message = f"Your cart total is equal to ${total:.2f}"
        self.tot.setText(str(message))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    cart = shop_cart()
    cart.show()
    sys.exit(app.exec_())