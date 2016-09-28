import tensorflow as tf

# Define a as constant
a = tf.constant(100, name='a')
# Define variable b
b = tf.Variable(a + 20, name='b')
# Define variable c
c = tf.Variable(a - 15, name='c')
# Define variable d
d = tf.Variable(a / 20, name='d')
# Define variable e
e = tf.Variable( a * a, name='e')

# Print equation objects
print(a)   #Tensor("a:0", shape=(), dtype=int32)
print(b)   #<tensorflow.python.ops.variables.Variable object at 0x101b642d0>
print(c)   #<tensorflow.python.ops.variables.Variable object at 0x1073296d0>
print(d)   #<tensorflow.python.ops.variables.Variable object at 0x106cb4ad0>
print(e)   #<tensorflow.python.ops.variables.Variable object at 0x106cb4ad0>



# Initialize all variables a.k.a create model
model = tf.initialize_all_variables()

# Run a TensorFlow Session for computing the values
with tf.Session() as session:
    session.run(model)
    print(session.run(a))  #100
    print(session.run(b))  #120
    print(session.run(c))  #85
    print(session.run(d))  #5
    print(session.run(e))  #10000