def biggest_plot(width, height, orig_area=None):

    if orig_area is None:

        orig_area = width*height
        print(orig_area)

    x, y = max(width, height), min(width, height) 

    if x%y == 0:

        return (((y,y), f"Squares= {orig_area//(y*y)}"))

    print("prior_x =", x) 
 
    prior_y = y

    y = (x%y)

    print("post_y =", y)

    x = prior_y

    print("post_x =", x)
     
    return biggest_plot(x,y, orig_area) 

