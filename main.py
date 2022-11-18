def main():
    source = ""
    baseAddress = "/home/esholland/workspace/github.com/esholland85/bookbot/"
    targetDir = "books/Frankenstein"
    address = baseAddress + targetDir

    with open(address) as f:

        source = f.read()

    def get_word_count(input_string):
        words = input_string.split()
        return(len(words))

    def count_occurrences(input_string):
        letter_count = {}
        lowercase = input_string.lower()
        #remove isalpha boolean from both if and elif to count special characters
        for l in lowercase:
            if l in letter_count and l.isalpha():
                letter_count[l] += 1
            elif l.isalpha():
                letter_count[l] = 1
        return letter_count

    def order_occurrences(input_dictionary):
        result = ""
        

        for i in range(0,len(input_dictionary)):
            highest_key = ''
            max_so_far = float('-inf')
            for e in input_dictionary:
                if input_dictionary[e] > max_so_far:
                    highest_key = e
                    max_so_far = input_dictionary[e]
            result += f"The \'{highest_key}\' character occurs {max_so_far} times \n"
            del input_dictionary[highest_key]

        return result

    print(f"--- Begin report of {targetDir} ---")
    print(f"{get_word_count(source)} words in the document")
    print("\n")
    #print(count_occurrences(source))
    print(order_occurrences(count_occurrences(source)))
    print("--- End report ---")

main()