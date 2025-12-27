from textnode import TextNode, TextType

def main(): 
    
    test_node = TextNode("Hello there!", TextType.TEXT, "http:localhost:8888")
    
    print(repr(test_node))

main()