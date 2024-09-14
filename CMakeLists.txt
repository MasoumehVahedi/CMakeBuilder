cmake_minimum_required(VERSION 3.12)
project(CMakeBuilder)

# Find the Python interpreter and its libraries
find_package(Python REQUIRED COMPONENTS Interpreter Development)

# Define the source files for your project
set(SOURCES
    src/main.py
    src/binary_tree.py
)

# Create a custom target to run the Python script
add_custom_target(run_python_script
    COMMAND python ${CMAKE_CURRENT_SOURCE_DIR}/src/main.py
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/src
    COMMENT "Running main.py script"
)

# Set the custom target as the default target
set_property(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR} PROPERTY VS_STARTUP_PROJECT run_python_script)


# Create the Python extension module
#add_library(BinaryTree MODULE ${SOURCES})

# Link against the Python libraries
#target_link_libraries(BinaryTree PRIVATE Python::Python)

