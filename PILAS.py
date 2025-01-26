// Conceptualización de estructuras de datos
// Estructuras revisadas: Pila, Cola, Lista Enlazada
/*
 * Pilas:
 * Una pila es una estructura de datos que sigue el principio LIFO (Last In, First Out), es decir, el último elemento en entrar es el primero en salir.
 * Operaciones principales: Push (insertar), Pop (eliminar) y Peek (consultar el elemento superior).
 * Uso: Balanceo de paréntesis, implementación de llamadas de funciones, algoritmos como el de Torres de Hanoi.
 *
 * Colas:
 * Una cola sigue el principio FIFO (First In, First Out), donde el primer elemento en entrar es el primero en salir.
 * Operaciones principales: Enqueue (insertar) y Dequeue (eliminar).
 * Uso: Sistemas de impresión, gestión de tareas en procesos, manejo de buffers.
 *
 * Listas enlazadas:
 * Una lista enlazada está formada por nodos, donde cada nodo contiene un valor y una referencia al siguiente nodo.
 * Tipos: Simplemente enlazada, doblemente enlazada, circular.
 * Uso: Implementación de estructuras dinámicas, manejo eficiente de memoria, realización de operaciones como inserciones y eliminaciones.
 */

using System;
using System.Collections.Generic;

class Program
{
    // Función para verificar si una expresión matemática tiene paréntesis balanceados
    static bool VerificarBalanceo(string expresion)
    {
        Stack<char> pila = new Stack<char>();

        foreach (char caracter in expresion)
        {
            if (caracter == '(' || caracter == '{' || caracter == '[')
            {
                // Agregar a la pila si es un paréntesis de apertura
                pila.Push(caracter);
            }
            else if (caracter == ')' || caracter == '}' || caracter == ']')
            {
                // Verificar si la pila está vacía o no coincide el paréntesis
                if (pila.Count == 0) return false;

                char tope = pila.Pop();
                if (!Coinciden(tope, caracter)) return false;
            }
        }

        // Si la pila está vacía, los paréntesis están balanceados
        return pila.Count == 0;
    }

    // Función para verificar si los paréntesis coinciden
    static bool Coinciden(char apertura, char cierre)
    {
        return (apertura == '(' && cierre == ')') ||
               (apertura == '{' && cierre == '}') ||
               (apertura == '[' && cierre == ']');
    }

    // Resolución del problema de las Torres de Hanoi
    static void TorresDeHanoi(int discos, string origen, string auxiliar, string destino)
    {
        if (discos == 1)
        {
            Console.WriteLine($"Mover disco de {origen} a {destino}");
        }
        else
        {
            TorresDeHanoi(discos - 1, origen, destino, auxiliar);
            Console.WriteLine($"Mover disco de {origen} a {destino}");
            TorresDeHanoi(discos - 1, auxiliar, origen, destino);
        }
    }

    static void Main(string[] args)
    {
        // Verificación de balanceo
        string expresion = "{7+(8*5)-[(9-7)+(4+1)]}";
        bool balanceado = VerificarBalanceo(expresion);
        Console.WriteLine(balanceado ? "Fórmula balanceada" : "Fórmula no balanceada");

        // Resolución de las Torres de Hanoi
        int numeroDeDiscos = 3;
        Console.WriteLine("Resolución de las Torres de Hanoi:");
        TorresDeHanoi(numeroDeDiscos, "Origen", "Auxiliar", "Destino");
    }
}
