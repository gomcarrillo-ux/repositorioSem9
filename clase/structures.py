from typing import List, Dict, Optional, Tuple

class DataItem:
    """Representa un elemento individual (Texto o Imagen)."""
    def __init__(self, item_type: str, content: str):
        self.type = item_type      # 'text' o 'image'
        self.content = content    # Cadena de texto o DataURL en Base64

    def to_dict(self) -> Dict[str, str]:
        return {
            'type': self.type,
            'content': self.content
        }


class Stack:
    """Implementación de Pila (LIFO: Last-In, First-Out)."""
    def __init__(self, capacity: int = 5):
        if capacity <= 0:
            raise ValueError("La capacidad debe ser mayor a cero.")
        self.capacity: int = capacity
        self._items: List[DataItem] = []

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def is_full(self) -> bool:
        return len(self._items) >= self.capacity

    def push(self, item_type: str, content: str) -> Tuple[bool, str]:
        if self.is_full():
            return False, "¡Error! Overflow: La pila está llena."
        self._items.append(DataItem(item_type, content))
        tipo_str = "Texto" if item_type == "text" else "Imagen"
        return True, f"¡Éxito! {tipo_str} apilado correctamente."

    def pop(self) -> Tuple[bool, Optional[Dict[str, str]], str]:
        if self.is_empty():
            return False, None, "¡Error! Underflow: La pila está vacía."
        popped_item = self._items.pop()
        tipo_str = "Texto" if popped_item.type == "text" else "Imagen"
        return True, popped_item.to_dict(), f"Elemento ({tipo_str}) desapilado con éxito."

    def peek(self) -> Tuple[bool, Optional[Dict[str, str]], str]:
        if self.is_empty():
            return False, None, "La pila está vacía."
        top_item = self._items[-1]
        tipo_str = "Texto" if top_item.type == "text" else "Imagen"
        return True, top_item.to_dict(), f"Tope actual de la pila ({tipo_str})."

    def get_items(self) -> List[Dict[str, str]]:
        return [item.to_dict() for item in self._items]

    def clear(self) -> None:
        self._items.clear()


class Queue:
    """Implementación de Cola (FIFO: First-In, First-Out)."""
    def __init__(self, capacity: int = 5):
        if capacity <= 0:
            raise ValueError("La capacidad debe ser mayor a cero.")
        self.capacity: int = capacity
        self._items: List[DataItem] = []

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def is_full(self) -> bool:
        return len(self._items) >= self.capacity

    def enqueue(self, item_type: str, content: str) -> Tuple[bool, str]:
        if self.is_full():
            return False, "¡Error! Overflow: La cola está llena."
        self._items.append(DataItem(item_type, content))
        tipo_str = "Texto" if item_type == "text" else "Imagen"
        return True, f"¡Éxito! {tipo_str} encolado al final."

    def dequeue(self) -> Tuple[bool, Optional[Dict[str, str]], str]:
        if self.is_empty():
            return False, None, "¡Error! Underflow: La cola está vacía."
        dequeued_item = self._items.pop(0)  # Remueve el primero en entrar (FIFO)
        tipo_str = "Texto" if dequeued_item.type == "text" else "Imagen"
        return True, dequeued_item.to_dict(), f"Elemento ({tipo_str}) desencolado del frente."

    def peek(self) -> Tuple[bool, Optional[Dict[str, str]], str]:
        if self.is_empty():
            return False, None, "La cola está vacía."
        front_item = self._items[0]
        tipo_str = "Texto" if front_item.type == "text" else "Imagen"
        return True, front_item.to_dict(), f"Frente de la cola ({tipo_str})."

    def get_items(self) -> List[Dict[str, str]]:
        return [item.to_dict() for item in self._items]

    def clear(self) -> None:
        self._items.clear()