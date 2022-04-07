from jinja2 import StrictUndefined, Template

# Evaluation
temp = """My name is {{NAME}}. 
I'm {{AGE}} year old.
{# This is comment let's see-#}
I love {{What}}. I work with {{COMPANY}}"""

data = {"NAME": "Shashank", "AGE": 23, "What": "Coding", "COMPANY": "GSlab"}
j2_template = Template(temp, undefined=StrictUndefined)
print(j2_template.render(data))
print("*" * 20)

temp2 = """I'm in the {% for i in range(5) %}
        Loop {{i-}}
        {% endfor %}
    """

j2_template = Template(temp2, undefined=StrictUndefined)
print(j2_template.render())


temp3 = """I'm {% if stat == True -%}
coding
{%-else-%}
sleeping
{%-endif%}"""

j2_template = Template(temp3, undefined=StrictUndefined)
print(j2_template.render(stat=True))


temp4 = """
{% macro bool_eval(value) -%}
{% if value -%}
True
{%- else -%}
False
{%- endif %}
{%- endmacro -%}

My one element list has bool value of: {{ bool_eval(my_list) }}
My one key dict has bool value of: {{ bool_eval(my_dict) }}
My short string has bool value of: {{ bool_eval(my_string) }}

My empty list has bool value of: {{ bool_eval(my_list_empty) }}
My empty dict has bool value of: {{ bool_eval(my_dict_empty) }}
My empty string has bool value of: {{ bool_eval(my_string_empty) }}


"""
data = {
    "my_list": ["list-element"],
    "my_dict": {"my_key": "my_value"},
    "my_string": "example string",
    "my_list_empty": [],
    "my_dict_empty": {},
    "my_string_empty": "",
}

j2_template = Template(temp4, undefined=StrictUndefined)
print(j2_template.render(data))

temp5 = """{% macro banner() -%}
banner motd ^
===========================================
|   This device is property of BigCorpCo  |
|   Unauthorized access is unauthorized   |
|  Unless you're authorized to access it  |
|  In which case play nice and stay safe  |
===========================================
^
{% endmacro -%}

{{ banner() }}{{ banner() }}{{ banner() }}"""
j2_template = Template(temp5, undefined=StrictUndefined)
print(j2_template.render())
