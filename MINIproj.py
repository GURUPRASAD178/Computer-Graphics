import cv2
import numpy as np

# Create a blank image
height, width = 700, 1500
road_color = (50, 50, 50)  # Dark gray for the road
background_color = (235, 206, 135)  # Light blue for the sky

# Initial position and speed of the cycle
position = [100, height - 80]
speed = [0, 0]
acceleration = 1


def draw_cycle(img, position):
    x, y = position

    # Draw wheels
    wheel_radius = 25
    cv2.circle(img, (x - 40, y + 20), wheel_radius, (0, 0, 0), 3)
    cv2.circle(img, (x + 40, y + 20), wheel_radius, (0, 0, 0), 3)
                #position of circles ,radius, thickness

    # Draw wheel spokes
    for i in range(0, 360, 45):
        angle_rad = np.deg2rad(i)
        cv2.line(img,
                 (int(x - 40 + wheel_radius * np.cos(angle_rad)), int(y + 20 + wheel_radius * np.sin(angle_rad))),
                 (int(x - 40 - wheel_radius * np.cos(angle_rad)), int(y + 20 - wheel_radius * np.sin(angle_rad))),
                 (0, 0, 0), 1)
        cv2.line(img,
                 (int(x + 40 + wheel_radius * np.cos(angle_rad)), int(y + 20 + wheel_radius * np.sin(angle_rad))),
                 (int(x + 40 - wheel_radius * np.cos(angle_rad)), int(y + 20 - wheel_radius * np.sin(angle_rad))),
                 (0, 0, 0), 1)

    # Draw frame
    cv2.line(img, (x + 40, y + 20), (x + 27, y - 35), (0, 0, 0), 2) #front
    cv2.line(img, (x - 40, y + 20), (x - 20, y - 25), (0, 0, 0), 2) #back
    cv2.line(img, (x - 25, y - 30), (x, y), (0, 0, 0), 2) #middle back
    cv2.line(img, (x + 27 ,y - 25), (x ,y), (0, 0, 0), 2) #middle front
    cv2.line(img, (x, y), (x - 40, y + 20), (0, 0, 0), 2)
    cv2.line(img, (x, y), (x + 40, y + 20), (0, 0, 0), 2)
    #cv2.line(img, (x - 20, y + 20), (x + 20, y + 20), (0, 0, 0), 2)

   

    # Draw handlebar
    cv2.line(img, (x + 27, y - 33), (x + 12, y - 46), (0, 0, 0), 2)
    cv2.line(img, (x + 27, y - 33), (x + 42, y - 20), (0, 0, 0), 2)
    #cv2.line(img, (x - 20, y - 40), (x - 10, y - 30), (0, 0, 255), 2)

    # Draw seat
    cv2.line(img, (x - 22, y - 25), (x + 27 , y - 25), (0, 0, 0), 2)
    
    cv2.line(img, (x - 30, y - 30), (x - 10, y - 30), (0, 0, 0), 2)

    # Draw pedals
    cv2.line(img, (x, y), (x, y + 10), (0, 0, 0), 2)
    cv2.line(img, (x, y + 10), (x - 5, y + 15), (0, 0, 0), 2)
    cv2.line(img, (x, y + 10), (x + 5, y + 15), (0, 0, 0), 2)


def draw_street_lights(img):
    light_color = (0, 255, 255)  # Yellow light
    pole_color = (0, 100, 100)  # Gray pole

    # Draw multiple street lights
    for i in range(100, width, 200):
        cv2.line(img, (i, height - 60), (i, height - 250), pole_color, 5)
        cv2.circle(img, (i, height - 260), 15, light_color, -1)


def main():
    global position, speed

    while True:
        img = np.full((height, width, 3), background_color, dtype=np.uint8)

        light_color = (0, 255, 255)
        cv2.circle(img,(150,150),10,light_color,250)
        
        # Draw the road
        cv2.rectangle(img, (0, height - 60), (width, height), road_color, -1)
        cv2.line(img, (0, height - 60), (1500, height - 60),(0 ,255 ,0 ), 5)
        cv2.line(img, (0, height - 30), (1500, height - 30),(255 ,255 ,255 ), 2)

        # Draw street lights
        draw_street_lights(img)

        # Draw the cycle
        draw_cycle(img, position)

        # Update the cycle's position
        position[0] += speed[0]
        position[1] += speed[1]

        # Check for boundaries
        if position[0] < 0:
            position[0] = 0
        elif position[0] > width:
            position[0] = width
        if position[1] < 0:
            position[1] = 0
        elif position[1] > height - 50:
            position[1] = height - 50

        cv2.imshow('Cycle Animation', img)

        # Handle key presses for controls
        key = cv2.waitKey(30) & 0xFF

        if key == 27:  # Press 'Esc' to exit
            break
        elif key == ord('w'):  # Move up
            speed[1] -= acceleration
        elif key == ord('x'):  # Move down
            speed[1] += acceleration
        elif key == ord('a'):  # Move left
            speed[0] -= acceleration
        elif key == ord('d'):  # Move right
            speed[0] += acceleration
        elif key == ord('s'):  # Stop
            speed = [0, 0]

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
