#include <Python.h>

/**
 * print_python_list- Prints some basic information about Python lists
 * @p: The Python list
 *
 * Return: nothing
 */

void print_python_list(PyObject *p)
{
	char *type = (((PyObject*)(p))->ob_type)->tp_name;
	int size = ((PyVarObject*)(p))->ob_size, counter = 0;
	long alloc = ((PyListObject *)(p))->ob_allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %ld\n", alloc);
	for (counter = 0; counter < size; counter++)
	{
		printf("Element %d: %s\n", counter, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(p[counter]);
		else if (strcmp(type, "float") == 0)
			print_python_float(p[counter]);
	}
}

/**
 * print_python_bytes- Prints some basic info about Python bytes
 * @p: A pointer to the python list
 *
 * Return: nothing
 */

void print_python_bytes(PyObject *p)
{
	int counter = 0;
	int size = ((PyVarObject*)(p))->ob_size;


	printf("[.] bytes object info\n");
	printf("  size: %d\n", size);
	printf("  trying string: %s\n", str);
	printf("  first %d bytes: ");

	for (counter = 0; counter < size; counter++)
	{
		printf("%c", str[counter]);
	}
}
