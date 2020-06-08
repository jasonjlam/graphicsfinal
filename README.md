# graphicsfinal

Jason Lam and Tejas Narayan

Period 4 and Period 5 (respectively)

# To use:

* Create an mdl file based on the available commands
* Place all files to be read into the files folder
* Run python main.py *<filename>* (or python3 if you so choose)
* Completed gif or image will be in the /gifs or /images subdirectory respectively

# Mesh
* Import .obj files from the files folder
* To use, add *mesh <filename>* where *<filename>* omits the file extension
* The mesh can be manipulated by any other MDL command

# Set
* Set a selected knob to a certain value
* To use, add *set <knob name> <value>*

# Save knobs
* Save the current knob values to a symbol in the symbol table
* To use, add *save_knobs knob list*

# Save coordinate system
* Save the current coordinate system on the top of the stack to a symbol in the symbol table
* To use, add *save_coord_system <name>*:
* Can be used as a parameter for polygons *(to be implemented later)*

# Many different types of interpolation for *vary*
* An extra parameter has been added to the vary command to change up interpolation
* Types of interpolation include linear, quadratic, cubic, logarithmic, and oscillation
* To use, add *vary ... <type>* where type is the kind of interpolation you want
* Vary still has functionality without a given type, and defaults to linear

# To do:
* Adding lights to the symbol table
* Varying types of shading
* Adding parameter to use saved coordinate systems instead of the stack
