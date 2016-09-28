import matplotlib.image as img
import matplotlib.pyplot as plt
import tensorflow as tf

# Load Image
filename = "fall.png"
image = img.imread(filename)

# Print image shape
print(image.shape) # (1080, 1080, 3)

width,height,depth = image.shape



#print(image) # Will print image array, uncomment if you want to see how is image represented

m= i = z = y = x = tf.Variable(image, name='x')


model = tf.initialize_all_variables()

with tf.Session() as session:

    # Mirror Image
    left = tf.slice(m, [0, 0, 0], [height, width/2, depth])
    right = tf.reverse(left, [False, True, False])
    m = tf.concat(1, [left, right])

    # Tranform 90 degree counter clockwise
    x = tf.transpose(x, perm=[1, 0, 2])

    # Flip Image
    y = tf.reverse_sequence(y, [width] * height, 1, batch_dim=0)

    # Rotate clockwise, flip new x
    z = tf.reverse_sequence(x, [width] * height, 1, batch_dim=0)

    # Upside down
    i = tf.transpose(z, perm=[1, 0, 2])

    session.run(model)
    counter_clock = session.run(x)
    flip = session.run(y)
    rotate = session.run(z)
    topdown = session.run(i)
    mirror = session.run(m)


plt.imshow(mirror)
plt.show()


plt.imshow(counter_clock)
plt.show()

plt.imshow(flip)
plt.show()

plt.imshow(rotate)
plt.show()

plt.imshow(topdown)
plt.show()





