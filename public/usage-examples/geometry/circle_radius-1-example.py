from splashkit import *

# Declare constants and variables
MAX_RADIUS = 250
window = open_window("Circle Radius", 600, 700)
arial = load_font("arial", "arial.ttf")

circle = circle_at(screen_center(), 100)
quadrant1 = rectangle_from(circle_x(circle), circle_y(circle) - circle_radius(circle), circle_radius(circle) + 1, circle_radius(circle) + 1)
quadrant2 = rectangle_from(circle_x(circle) - circle_radius(circle), circle_y(circle) - circle_radius(circle), circle_radius(circle) + 1, circle_radius(circle) + 1)
quadrant3 = rectangle_from(circle_x(circle) - circle_radius(circle), circle_y(circle), circle_radius(circle) + 1, circle_radius(circle) + 1)
quadrant4 = rectangle_from(circle_x(circle), circle_y(circle), circle_radius(circle) + 1, circle_radius(circle) + 1)

quadrant_clicked = 0
pt_pt_angle = 0

while (not window_close_requested(window)):
    process_events()

    # User input to change radius size
    if (key_down(KeyCode.up_key) and circle_radius(circle) < MAX_RADIUS):
        circle.radius += 1
    if (key_down(KeyCode.down_key) and circle_radius(circle) > 10):
        circle.radius -= 1

    # Click left mouse button to remove quadrant of circle in mouse location
    pt_pt_angle = point_point_angle(screen_center(), mouse_position())
    if (mouse_clicked(MouseButton.left_button)):
        if (pt_pt_angle < 0 and pt_pt_angle >= -90):
            quadrant_clicked = 1
        if (pt_pt_angle < -90 and pt_pt_angle >= -180):
            quadrant_clicked = 2
        if (pt_pt_angle < 180 and pt_pt_angle >= 90):
            quadrant_clicked = 3
        if (pt_pt_angle < 90 and pt_pt_angle >= 0):
            quadrant_clicked = 4

    # Press escape key to show whole circle
    if (key_typed(KeyCode.escape_key)):
        quadrant_clicked = 0

    # Show/hide segment cut-out
    if (key_down(KeyCode.space_key)):
        clear_screen(color_light_gray())
    else:
        clear_screen(color_white())

    # Draw the Circle and segment cut-out if clicked
    fill_circle_record(color_orange(), circle)
    match (quadrant_clicked):
        case 1:
            quadrant1 = rectangle_from(circle_x(circle), circle_y(circle) - circle_radius(circle), circle_radius(circle) + 1, circle_radius(circle) + 1)
            fill_rectangle_record(color_white(), quadrant1)
        case 2:
            quadrant2 = rectangle_from(circle_x(circle) - circle_radius(circle), circle_y(circle) - circle_radius(circle), circle_radius(circle) + 1, circle_radius(circle) + 1)
            fill_rectangle_record(color_white(), quadrant2)
        case 3:
            quadrant3 = rectangle_from(circle_x(circle) - circle_radius(circle), circle_y(circle), circle_radius(circle) + 1, circle_radius(circle) + 1)
            fill_rectangle_record(color_white(), quadrant3)
        case 4:
            quadrant4 = rectangle_from(circle_x(circle), circle_y(circle), circle_radius(circle) + 1, circle_radius(circle) + 1)
            fill_rectangle_record(color_white(), quadrant4)

    # Draw other shapes and instructions
    draw_rectangle(color_gray(), 50, 100, 500, 500)
    draw_line(color_gray(), screen_width() / 2, 100, screen_width() / 2, 600)
    draw_line(color_gray(), 50, screen_height() / 2, 550, screen_height() / 2)
    draw_text("Instructions", color_red(), arial, 16, 50, 10)
    draw_text("1. Use the up/down arrow keys to change the radius of the circle.", color_blue(), arial, 14, 50, 40)
    draw_text("2. Click in a quadrant to remove the segment of the circle. Escape key to reset.", color_blue(), arial, 14, 50, 65)
    draw_text("Psst! Hold Space bar to see how it works!", color_blue(), arial, 12, 50, 630)
    draw_text("Circle Radius: " + str(int(circle_radius(circle))), color_green(), arial, 24, 320, 620)
    refresh_screen_with_target_fps(60)

close_window(window)
free_font(arial)