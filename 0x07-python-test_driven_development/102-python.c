#include "python.h"
/**
 * print_python_string - This displays python strings information
 * @p: PyObject string
 */
void print_python_string(PyObject *p)
{
	long int ken;

	fflush(stdout);
	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf(" [ERROR] Invalid String object\n")
		return;
	}
	ken = ((PyASCIIobject *)(p))->length;
	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf(" type: compact ascii\n");
	else
		printf(" type: compact unicode object\n");
	printf(" length: %ld\n", ken);
	printf(" value: %ls\n", PyUnicode_AsWideCharString(p, &ken));
