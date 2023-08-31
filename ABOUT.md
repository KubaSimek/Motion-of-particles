# Simulation of the motion of 2D particles in a box

**Created by Jakub Šimek**

## Description of the problem

Create a Python program that animates a simulation of particles motion in a 2D box.
It should be possible to select particles of different sizes and masses, place the particles however we want in the box, and select the velocity of the particle in any direction.

The particles must move and bounce elastically from each other and from the walls.

Optimize the problem numerically so that it does not chop during the animation due to long calculations.

## Information for users

Run the gui.py file to launch the program. 
A user interface will open that allows you to start creating a simulation or learn basic information about the program.

You can add particles to the simulation at any position in the box. 
The position of the particle is selected by clicking on the desired place in the box.
It is possible to repeat the position selection after clicking again.

Next, the size of the radius of the particle is selected. The size of the entire box is 10x10 and the radius is also selected in the same "units".
The maximum size is 5 units, but in practice it is better to choose a radius smaller than 3.

_Unfortunately, the program does not check whether the particle fits in the box and does not extend into other particles, so you need to choose radius and position carefully to avoid problems._

Next, the particle velocity is selected. The velocity is selected in the directions of the X and Y axes. It is recommended to enter floats from -100 to 100 to avoid unexpected bugs, but a speed greater than 200 also works in practice.

_This method of velocity selection is slightly impractical, but it is enough to create a simulation._

Finally, the mass of the particle is selected simply by entering a positive float value.

It is now possible to add another particle to the simulation or run the simulation

_The problem sometimes arises if you want to go back a step during the selection of particle parameters. The program does not offer this option._

To create another simulation, the program needs to be closed and started again.

##  Technical information about the program

The code itself is divided into three parts (three files).
Next, I will describe the basic structure and ideas of all these parts.

### Main program - animation

Particles with their parameters are defined in this program, and animation is also created in this program.

In this code we use the numpy and matplotlib library along with additional libraries that are used for animation and connecting with Tkinter (GUI)

At the beginning is the Particle class, which contains the properties of each individual particle and has a method for listing these properties and plotting the particles on the canvas. Parameters of the type array are also created with the coordinates of the velocity and position of the particles, which are used when calculating the change in direction and magnitude of the velocity during collisions to reduce the computing time.

Next, there is the Particles class, which collects all the particles and its method directly performs the animation. This class is just a list with elements of type "Particle". It also contains methods to add a particle and delete particles, as well as to initialize the animation on the canvas.

The animation method is run from a GUI file. First, the box on which the simulation will take place is "shaped". For example, setting the size, line width, etc.

All particles stored in the Particles class are plotted. Their movement (animation) is ensured by changing their coordinates.
Particles are shown as points with a given radius.

Next, a function is defined that changes the position of all particles to which they move (depending on the velocity) in time dt.

An Update function is defined, which is called directly as an argument to the FuncAnimation function from the matplotlib library.
In this function, the time change is first set appropriately so that the animation is smooth.
Next, two functions are launched that detect whether a collision has occurred and, if necessary, change the velocities of the particles. These functions will be written about in the next section.
The velocity and position coordinantes are changed also in the arrays.
Next, the position of the particles is changed and these particles are plotted on the canvas.

At the end, only the FuncAnimation function from the matplotlib library is run, which provides the animation.

### Collision functions
In this part of the program called bounce_functions, there are functions that take care of finding out if there has been a collision and, if necessary, solving this collision by changing the particle velocities.

First, there's a function that takes care of wall collisions.
This function is called from the Main_program.py
This function checks if some particle is touching a wall (or is little bit "in a wall")
and then change the sign of the velocity of the particle in corresponding direction. 
For example if the particle touches the right wall, the velocity in the X direction should change the sign to "-" to simulate the collision.
After the changing of the velicity, the corresponding position coordinant of the particle is set as the radius of the particle.
This is how the program prevents bugs that could occur if a particle hits a wall at high speed and before the program records it,it would get further into the wall and when the speed changes, the program would record the collision again because the particle does not have time to leave the wall and therefore the particle would remain stuck in the wall.

Next, there is a function that detects whether the particles are touching. Using the Pythagorean theorem, we know the distance between the centers of two particles and then this distance is compared to the sum of the radii of these particles. If the sum of the radii is greater, then the particles touch (they are a little inside each other) and vice versa.

Next, there is a function that is key to reducing the numerical complexity. This function is called at the beginning of the program and creates a list of all pairs of particles. So if we need to check the collision of every pair of particles at each frame of the animation, we just need to iterate through this list. If there are "n" particles, then there are (n choose 2) of these pairs, so it is necessary to perform only n<sup>2</sup> operations, which are used to solve particle collisions, for each frame.

Finally, there is a function that goes through the list of pairs at each step of the animation and detects if a particle collision has occurred. In case of particle collision, the program calculates the new individual particle velocities after the collision using the law of conservation of energy and momentum, more on [Wikipedia](https://en.wikipedia.org/wiki/Elastic_collision).

After the changing of the velicities, particles are moved so they just touching again.(not intersect)
We select one particle and move the second particle in the direction given by the straight line between the centers
to the distance of the sum of both radii from the center of the second particle. 
This is done by first finding the line leading from the centers of the particles, finding the length of this line, normalizing it and scaling it to the size of the sum of the particle radii.
It helps avoid the same bugs described in the function that deals with wall collisions.

All of this is done using the numpy library using arrays to increase computational efficiency.

### Graphical User Interface
In this section I will describe the code for the GUI.
I used the Tkinter library to create the GUI.

First, the window and canvas sizes are defined and the colours that will be used in the program are selected.

Images of buttons, backgrounds and other elements are uploaded. Buttons always have two different images that will switch between depending on whether the cursor is on the button or not.

Next, some variables are established. One variable is a list into which all the elements on the window are stored so that they can be handled together. All plotted particles are stored in the next variable.
Other boolean variables help us to know in which phase of particle parameter selection we are currently in.
We add other variables.
Through the process of adding the particle we will change these variables and after selecting last variable (mass) 
it will add the particle with its properties to the set of all particles.

Next, the user input process is programmed. For example, for the program to know where, depending on the box, the pointer is when selecting a position and to respond to a click in the box to confirm the selection of the position (or to reselect the position).

Widgets are added to the canvas and placed in the desired location. Text widgets are also created and placed.

The following are the functions that are called when the individual buttons are clicked. This is always followed by deleting all elements on the canvas and only making the required elements visible.

When selecting particles, individual parameters are added and finally the particle is added to the set of all particles. After clicking the SIMULATION button, the animation from the main_program file will start along with the desired group of particles.

Next, there are functions that are used as commands for changing the style of the button when mouse pointer enters the button.
And finally binding these function to buttons.



This is information about the structure of the program. 

When creating the program, I used answers to various questions on StackOverflow and Wikipedia to help with collision calculations.











