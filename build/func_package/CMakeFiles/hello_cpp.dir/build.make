# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/vboxuser/demo_2/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/vboxuser/demo_2/build

# Include any dependencies generated for this target.
include func_package/CMakeFiles/hello_cpp.dir/depend.make

# Include the progress variables for this target.
include func_package/CMakeFiles/hello_cpp.dir/progress.make

# Include the compile flags for this target's objects.
include func_package/CMakeFiles/hello_cpp.dir/flags.make

func_package/CMakeFiles/hello_cpp.dir/src/hello_cpp.cpp.o: func_package/CMakeFiles/hello_cpp.dir/flags.make
func_package/CMakeFiles/hello_cpp.dir/src/hello_cpp.cpp.o: /home/vboxuser/demo_2/src/func_package/src/hello_cpp.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/vboxuser/demo_2/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object func_package/CMakeFiles/hello_cpp.dir/src/hello_cpp.cpp.o"
	cd /home/vboxuser/demo_2/build/func_package && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/hello_cpp.dir/src/hello_cpp.cpp.o -c /home/vboxuser/demo_2/src/func_package/src/hello_cpp.cpp

func_package/CMakeFiles/hello_cpp.dir/src/hello_cpp.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/hello_cpp.dir/src/hello_cpp.cpp.i"
	cd /home/vboxuser/demo_2/build/func_package && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/vboxuser/demo_2/src/func_package/src/hello_cpp.cpp > CMakeFiles/hello_cpp.dir/src/hello_cpp.cpp.i

func_package/CMakeFiles/hello_cpp.dir/src/hello_cpp.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/hello_cpp.dir/src/hello_cpp.cpp.s"
	cd /home/vboxuser/demo_2/build/func_package && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/vboxuser/demo_2/src/func_package/src/hello_cpp.cpp -o CMakeFiles/hello_cpp.dir/src/hello_cpp.cpp.s

# Object files for target hello_cpp
hello_cpp_OBJECTS = \
"CMakeFiles/hello_cpp.dir/src/hello_cpp.cpp.o"

# External object files for target hello_cpp
hello_cpp_EXTERNAL_OBJECTS =

/home/vboxuser/demo_2/devel/lib/func_package/hello_cpp: func_package/CMakeFiles/hello_cpp.dir/src/hello_cpp.cpp.o
/home/vboxuser/demo_2/devel/lib/func_package/hello_cpp: func_package/CMakeFiles/hello_cpp.dir/build.make
/home/vboxuser/demo_2/devel/lib/func_package/hello_cpp: func_package/CMakeFiles/hello_cpp.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/vboxuser/demo_2/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable /home/vboxuser/demo_2/devel/lib/func_package/hello_cpp"
	cd /home/vboxuser/demo_2/build/func_package && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/hello_cpp.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
func_package/CMakeFiles/hello_cpp.dir/build: /home/vboxuser/demo_2/devel/lib/func_package/hello_cpp

.PHONY : func_package/CMakeFiles/hello_cpp.dir/build

func_package/CMakeFiles/hello_cpp.dir/clean:
	cd /home/vboxuser/demo_2/build/func_package && $(CMAKE_COMMAND) -P CMakeFiles/hello_cpp.dir/cmake_clean.cmake
.PHONY : func_package/CMakeFiles/hello_cpp.dir/clean

func_package/CMakeFiles/hello_cpp.dir/depend:
	cd /home/vboxuser/demo_2/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/vboxuser/demo_2/src /home/vboxuser/demo_2/src/func_package /home/vboxuser/demo_2/build /home/vboxuser/demo_2/build/func_package /home/vboxuser/demo_2/build/func_package/CMakeFiles/hello_cpp.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : func_package/CMakeFiles/hello_cpp.dir/depend

