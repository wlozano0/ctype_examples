/*--------------------------------------------------------------------------------------*
 * dllmain.c																			*
 *																						*
 * Version 1.0.0																	    * 
 *																						*
 * Copyright (c) Microtrol S.R.L. 2003													*
 * All rigthts reserved.																*
 *																						*
 * September 2003																		*
 *--------------------------------------------------------------------------------------*
 * Comentarios																			*
 *																						*
 *	1) 2/9/03	OK																		*
 *--------------------------------------------------------------------------------------*/

#include <windows.h>
#include <process.h>
#include <time.h>
#include <stdio.h>

// Ptototipos de funciones utilizadas en este archivo

BOOL WINAPI DllMain (HANDLE, DWORD, LPVOID);
BOOL DllAttach(void);
void DllDetach(void);

// Variables globales

/*--------------------------------------------------------------------------------------*
 * DllMain																				*
 *																						*
 * Esta funcion es el punto de entrada a la DLL, llamada toda vez que un proceso utili-	*
 * za la DLL por primera vez o que el ultimo proceso deja de utilizarla.				*
 * Tambien es llamada toda vez que un thread de un dado proceso utiliza la libreria por	*
 * primera vez o cuando termina un thread que hacia uso de la misma.					*
 * Devuelve TRUE si se completa correctamente la operacion y FALSE en caso contrario	*
 *--------------------------------------------------------------------------------------*/
 
BOOL WINAPI DllMain (HANDLE hDll, DWORD dwReason, LPVOID lpReserved)
{
	BOOL bRc;

	bRc = TRUE;

	switch (dwReason)
	{
		case DLL_PROCESS_ATTACH:			// El proceso levanta la DLL
			bRc = DllAttach();
			if(!bRc)
				DllDetach();
			break;

		case DLL_PROCESS_DETACH:			// El ultimo proceso termina el uso de
			DllDetach();					// la DLL
			break;

	    case DLL_THREAD_ATTACH:				// Cualquier thread de un proceso comienza o
		case DLL_THREAD_DETACH:				// termina el uso de la DLL
			break;

		default:
			break;
	} 

	return bRc;
}

/*--------------------------------------------------------------------------------------*
 * DllAttach()																			*
 *																						*
 * Esta funcion es llamada por el primer proceso que hace uso de la DLL.				*
 * Inicializa todos los recursos necesarios.											*
 * Devuelve TRUE si completa correctamente la inicializacion y FALSE en caso contrario	*
 *--------------------------------------------------------------------------------------*/

BOOL DllAttach(void)
{
	return TRUE;
	
}

/*--------------------------------------------------------------------------------------*
 * DllDetach()																			*
 *																						*
 * Esta funcion es llamada cuando el ultimo proceso deja de utilizar la DLL o si el		*
 * proceso de inicializacion falla y deben dealocarse los recursos.						*
 * No devuelve un valor																	*
 *--------------------------------------------------------------------------------------*/

void DllDetach(void)
{

}

