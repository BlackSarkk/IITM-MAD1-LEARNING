from jinja2 import Template

janapith_data = [
    {"year": 1965, "awardees" : "G. Sankara Kurup", "language":"Malayalam"} ,
    {"year": 1966, "awardees" : "Tarashankar Bandopadhyaya", "language":"Bengali"} ,
    {"year": 1967, "awardees" : "Kuppali Venkatappagowda Puttappa", "language":"Kannada"} ,
]


def main():
    tempHTML = open('boilerPlate.jinja2')   # "r" wont work here
    temp = Template(tempHTML.read())        # so need to use .read()
    tempHTML.close()

    # print(temp.render(janapith_data=janapith_data))
    my_html_document_file = open('janapith.html', 'w')
    my_html_document_file.write(temp.render(janapith_data=janapith_data))
    my_html_document_file.close()

if __name__ == "__main__":
    main()