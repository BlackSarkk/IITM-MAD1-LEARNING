
#*********************************************
#*********************************************
#*********************************************

# Using format specifiers would become hectic to manage stuffs
# So we're gonna use a templating engine called jinja2

# do: pip3 install jinja2
#   : pip freeze > requirements.txt

from jinja2 import Template

TEMPLATE = """Hello {{ name }}"""   

def main():
    temp = Template(TEMPLATE)
    print(temp.render(name="Rahul"))


if __name__ == "__main__":    
    main()
