from model import Model
from view import View
from controller import Controller

def main():
    model = Model()
    view = View()
    controller = Controller(model, view)
    view.set_controller(controller)
    view.mainloop()

if __name__ == "__main__":
    main()