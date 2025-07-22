import cv2

image = input("Enter img loc: ")

image = cv2.imread(image)

if image is None:
    print("Error: Could not load image.")
    exit()

print("\nWhat would u like to draw?")
print("1. Line")
print("2. Rectangle")
print("3. Circle")
print("4. Text")

choice = input("Enter choice: ")

if choice == "1":
    print("Enter coordinates for the line (x1 y1 x2 y2):")
    x1 = int(input("x1: "))
    y1 = int(input("y1: "))
    x2 = int(input("x2: "))
    y2 = int(input("y2: "))
    color = (0, 255, 0)
    thickness = 2
    image = cv2.line(image, (x1, y1), (x2, y2), color, thickness)

elif choice == "2":
    print("Enter top-left and bottom-right corners for the rectangle (x1 y1 x2 y2):")
    x1 = int(input("x1: "))
    y1 = int(input("y1: "))
    x2 = int(input("x2: "))
    y2 = int(input("y2: "))
    color = (255, 0, 0)
    thickness = 2
    image = cv2.rectangle(image, (x1, y1), (x2, y2), color, thickness)

elif choice == "3":
    print("Enter center and radius for the circle:")
    x = int(input("Center x: "))
    y = int(input("Center y: "))
    r = int(input("Radius: "))
    color = (0, 0, 255)  # Red
    thickness = 2
    image = cv2.circle(image, (x, y), r, color, thickness)

elif choice == "4":
    text = input("Enter the text to put: ")
    x = int(input("x: "))
    y = int(input("y: "))
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    color = (0, 255, 255)
    thickness = 2
    image = cv2.putText(image, text, (x, y), font, font_scale, color, thickness, cv2.LINE_AA)

else:
    print("Invalid choice.")
    exit()

cv2.imshow("Modified Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

save_choice = input("Do u want to save the image? (yes/no): ").lower()

if save_choice == "yes":
    output_name = input("Enter output file name: ")
    success = cv2.imwrite(output_name, image)
    if success:
        print(f"Image saved as {output_name}")
    else:
        print("Error: Could not save the image.")
else:
    print("Image not saved.")