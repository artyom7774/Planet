import tkinter
import random
import json

with open("files/files/quiz.json", "r", encoding="utf-8") as file:
    quiz = json.load(file)

root = tkinter.Tk()
root.title("Question")
root.resizable(False, False)
root.geometry("500x600+200+100")

variables = {
    "checkbox_0": tkinter.IntVar(),
    "checkbox_1": tkinter.IntVar(),
    "checkbox_2": tkinter.IntVar(),
    "checkbox_3": tkinter.IntVar(),

    "objects": {
        "text": [],
        "entry": [],
        "button": [],
        "checkbox": []
    }
}

texts = [
    "name: ",
    "question: ",
    "     1: ",
    "     2: ",
    "     3: ",
    "     4: "
]

entryes = [
    0, 0, 0, 0, 0, 0
]

buttons = [
    "Удалить",
    "Сохранить",
    "Получить",
    "Очистить"
]


def button_function(index):
    question = {
        "name": variables["objects"]["entry"][0].get(),
        "question": variables["objects"]["entry"][1].get(),
        "time": 30,
        "answers": [
            {
                "answer": 1 if variables["checkbox_0"].get() == 1 else 0,
                "text": variables["objects"]["entry"][2].get()
            },
            {
                "answer": 1 if variables["checkbox_1"].get() == 1 else 0,
                "text": variables["objects"]["entry"][3].get()
            },
            {
                "answer": 1 if variables["checkbox_2"].get() == 1 else 0,
                "text": variables["objects"]["entry"][4].get()
            },
            {
                "answer": 1 if variables["checkbox_3"].get() == 1 else 0,
                "text": variables["objects"]["entry"][5].get()
            }
        ]
    }

    print(question)

    if index == 0:
        if question["name"] in quiz:
            del quiz[question["name"]]

            variables["error_text"].config(text="Complited!")

        else:
            variables["error_text"].config(text="Name not found!")

    if index == 1:
        if question["name"] in quiz:
            variables["error_text"].config(text="Name already available!")

        else:
            quiz[question["name"]] = question

            variables["error_text"].config(text="Complited!")

    if index == 2:
        if question["name"] not in quiz:
            variables["error_text"].config(text="Name not found!")

        else:
            question = quiz[question["name"]]

            # delete

            variables["objects"]["entry"][1].delete(0, tkinter.END)

            variables["objects"]["entry"][2].delete(0, tkinter.END)
            variables["objects"]["entry"][3].delete(0, tkinter.END)
            variables["objects"]["entry"][4].delete(0, tkinter.END)
            variables["objects"]["entry"][5].delete(0, tkinter.END)

            # insert

            variables["objects"]["entry"][1].insert(0, question["question"])

            variables["objects"]["entry"][2].insert(0, question["answers"][0]["text"])
            variables["objects"]["entry"][3].insert(0, question["answers"][1]["text"])
            variables["objects"]["entry"][4].insert(0, question["answers"][2]["text"])
            variables["objects"]["entry"][5].insert(0, question["answers"][3]["text"])

            for i in range(4):
                variables[f"checkbox_{i}"].set(value=int(question["answers"][i]["answer"]))

    if index == 3:
        variables["objects"]["entry"][1].delete(0, tkinter.END)

        variables["objects"]["entry"][2].delete(0, tkinter.END)
        variables["objects"]["entry"][3].delete(0, tkinter.END)
        variables["objects"]["entry"][4].delete(0, tkinter.END)
        variables["objects"]["entry"][5].delete(0, tkinter.END)

        for i in range(4):
            variables[f"checkbox_{i}"].set(value=0)

    with open("files/files/quiz.json", "w", encoding="utf-8") as file:
        file.write(json.dumps(quiz, indent=4))


variables["error_text"] = tkinter.Label(root, text="", font=("Arial Blood", 12), fg="red")
variables["error_text"].place(x=5, y=450)

for i, text in enumerate(texts):
    variables["objects"]["text"].append(tkinter.Label(root, text=text, font=("Arial Blood", 14)))
    variables["objects"]["text"][i].place(x=5, y=5 + i * 25)

for i, entry in enumerate(entryes):
    variables["objects"]["entry"].append(tkinter.Entry(width=48))
    variables["objects"]["entry"][i].place(x=200, y=10 + i * 25)

variables["objects"]["button"].append(tkinter.Button(root, width=68, text=buttons[0], command=lambda: button_function(0)))
variables["objects"]["button"][0].place(x=7, y=510 + 0 * 30)

variables["objects"]["button"].append(tkinter.Button(root, width=68, text=buttons[1], command=lambda: button_function(1)))
variables["objects"]["button"][1].place(x=7, y=510 + 1 * 30)

variables["objects"]["button"].append(tkinter.Button(root, width=68, text=buttons[2], command=lambda: button_function(2)))
variables["objects"]["button"][2].place(x=7, y=510 + 2 * 30)

variables["objects"]["button"].append(tkinter.Button(root, width=68, text=buttons[3], command=lambda: button_function(3)))
variables["objects"]["button"][3].place(x=7, y=510 + -1 * 30)


for i in range(4):
    variables["objects"]["checkbox"].append(tkinter.Checkbutton(root, variable=variables[f"checkbox_{i}"], onvalue=1, offvalue=0))
    variables["objects"]["checkbox"][i].place(x=5, y=82 - 25 + i * 25)

root.mainloop()
