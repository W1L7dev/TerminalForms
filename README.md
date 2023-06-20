# TerminalForms

## Add forms to your terminal applications

---

### Installation

```bash
pip install terminal forms
```

> note: Depending on your python installation, the command mayt vary. For example, if you are using python3, you may need to use `pip3` instead of `pip`.

### Usage

```python
from terminalforms import Form, Field, Checkbox, Radio, Select, Text, Password, Submit

form = Form(
    title="Example Form",
    description="Please fill out the following information:",
    content=[
        Text("Welcome to the example form!"),
        Field("Name"),
        Checkbox("Agreement", "Do you agree to the terms and conditions?"),
        Select("Fruit", "Select your favorite fruit:", ["Apple", "Banana", "Orange"]),
        Radio("Gender", "Select your gender:", ["Male", "Female", "Other"]),
        Password("Password"),
        Submit("Submit")
    ]
)

form.show()
answers = form.get_all()
print(answers)
name = form.get("Name")
print(name)
```

### Documentation

#### Form

##### Parameters

- `title` - The title of the form
- `description` - The description of the form
- `content` - The content of the form

##### Methods

- `show()` - Show the form
- `get(name)` - Get the value of a field
- `get_all()` - Get all the values of the fields
- `set(name, value)` - Set the value of a field
- `clear()` - Clear all the values of the fields

#### Field

##### Parameters

- `name` - The name of the field
- `value` - The value of the field

##### Methods

- `ask()` - Ask the user for the value of the field

#### Text

##### Parameters

- `text` - The text of the text

##### Methods

- `text()` - Show the text

#### Checkbox

##### Parameters

- `name` - The name of the checkbox
- `question` - The question of the checkbox

##### Methods

- `ask()` - Ask the user for the value of the checkbox

#### Radio

##### Parameters

- `name` - The name of the radio
- `question` - The question of the radio
- `options` - The options of the radio

##### Methods

- `ask()` - Ask the user for the value of the radio

#### Select

##### Parameters

- `name` - The name of the select
- `question` - The question of the select
- `options` - The options of the select

##### Methods

- `ask()` - Ask the user for the value of the select

#### Password

##### Parameters

- `name` - The name of the password
- `value` - The value of the password
- `mask` - The mask of the password

##### Methods

- `ask()` - Ask the user for the value of the password

#### Submit

##### Parameters

- `name` - The name of the submit

##### Methods

- `ask()` - Ask the user for the value of the submit

### License

[MIT License](LICENSE)
