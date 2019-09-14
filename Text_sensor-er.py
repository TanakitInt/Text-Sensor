print("Simple text file sensor-er")
print("For experiment and privacy purposes")
print("By : TanakitInt")
print("")

try:
    def replace():
        #promt user input
        print("Please enter text file name (with \".TXT\" extension) : ")
        fileName = str(input())

        print("Please enter text replacer (ONLY 1 Character) : ")
        replacer = str(input())

        #Universal encoder for all language supported
        text = open(fileName, encoding="utf-8")
        text = text.read()

        #English alphabet only
        #with open(fileName) as file:
        #    text = file.read()

        storage = []
        #condition check for eah alphabet
        for i in text:
            if i == '\n':
                i = '\n'
                storage.append(i)

            elif i == " ":
                i = " "
                storage.append(i)

            else:
                i = replacer
                storage.append(i)

        #convert list to text
        newText = ''.join(storage)

        #write into new file and print it.
        print("Please enter output file name (with \".TXT\" extension) : ")
        outputFileName = str(input())

        with open(outputFileName, 'w') as outputFile:
            outputFile.write(newText)

        with open(outputFileName, 'r') as outputFile:
            preview = outputFile.read(1000)

        print("")
        print(outputFileName + " file preview : ")
        print("")
        print(preview)

    def main():
        #main function here
        userPrompt = str(input("Continue to run program (Y/N): "))
        if userPrompt in ["y", "Y", "1", "Yes", "yes"]:
            replace()

        elif userPrompt in ["n", "N", "0", "No", "no"]:
            quit()

        else:
            print("Now you don't")
            main()

    main()

except Exception as e:
    print("Error! " + str(e))
    main()
