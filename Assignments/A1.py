import cv2

image_location = input("Enter the location of the image: ")

image = cv2.imread(image_location)

if image is None:
    print("Error")
else:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    op = input("What u want to do?\n1. Show\n2. Save\n ")

    if op == "1":
        cv2.imshow("Grayscale Image", gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif op == "2":
        output_name = input("Enter o/p file name : ")
        cv2.imwrite(output_name, gray)
        print(f"Image saved as {output_name}")
    else:
        print("Invalid input.")
