#include <stdio.h>
#include <stdlib.h>
#include "python3.8/Python.h"

/**
 * print_python_list_info- Prints some basic info about Python lists
 * @p: A pointer to the Python list
 *
 * Return: Nothing
 */

void print_python_list_info(PyObject *p)
{
	int size, counter;

	size = PyList_Size(p);

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (counter = 0; counter < size; counter++)
	{
		printf("Element %d: %s\n", counter, Py_TYPE(PyList_GetItem(p, counter))->tp_name);
	}
}
