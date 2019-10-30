#!/usr/bin/env python3

from typing import Any, Union


class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def set_order(self, order: int) -> None:
        self.order = order

    def peek_order(self) -> int:
        return self.order

    def __str__(self) -> str:
        return f"{self.name}"


class Node:
    def __init__(self, data: Any):
        self.data = data
        self.next_node = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __str__(self) -> str:
        current = self.head
        string = f""
        while current.next_node is not None:
            string += f"{current.data} -> "
            current = current.next_node
        return string + "END"

    def is_empty(self) -> bool:
        if self.head is None:
            return True
        else:
            return False

    def insert(self, item: Any) -> None:
        if self.is_empty():
            self.head = Node(item)
            self.tail = self.head
        else:
            new_node = Node(item)
            self.tail.next_node = new_node
            self.tail = self.tail.next_node

    def remove(self) -> Any:
        if self.head is None:
            raise ("Empty LinkedList!")
        else:
            data = self.head.data
            self.head = self.head.next_node
            return data

    def peak(self):
        return self.head.data


class Dog(Animal):
    def __init__(self, name: str):
        super().__init__(name)


class Cat(Animal):
    def __init__(self, name: str):
        super().__init__(name)


class AnimalQueue:
    def __init__(self) -> None:
        self.dogs = LinkedList()
        self.cats = LinkedList()
        self.order = 0

    def enqueue(self, animal: Union[Dog, Cat]) -> None:
        if not isinstance(animal, (Dog, Cat)):
            raise Exception("Expected Dog or Cat!")
        else:
            animal.set_order(self.order)
            self.order += 1
            if isinstance(animal, Dog):
                self.dogs.insert(animal)
            elif isinstance(animal, Cat):
                self.cats.insert(animal)

    def dequeAny(self) -> Union[Dog, Cat]:
        if self.dogs.is_empty():
            return self.dequeCat()
        elif self.cats.is_empty():
            return self.dequeDog()

        if self.dogs.head.data.peek_order() > self.cats.head.data.peek_order():
            return self.dequeCat()
        else:
            return self.dequeDog()

    def print_cats(self) -> str:
        string = ""
        cat = self.cats.head
        while cat is not None:
            string += f"{cat.data.name} {cat.data.peek_order()} | "
            cat = cat.next_node
        return string

    def dequeDog(self) -> Dog:
        return self.dogs.remove()

    def dequeCat(self) -> Cat:
        return self.cats.remove()


def main():
    q = AnimalQueue()
    dogs = [Dog("d1"), Dog("d2"), Dog("d3")]
    cats = [Cat("c1"), Cat("c2"), Cat("c3")]
    both = []
    while cats != []:
        both.append(cats.pop())
        both.append(dogs.pop())
    [q.enqueue(animal) for animal in both]

    string = ""
    for anim in both:
        string += f"{anim.name} {anim.order} | "
    print(string)
    # print(q.print_cats())
    get = q.dequeDog()
    print(get.order,get.name)
    get = q.dequeAny()
    print(get.order,get.name)


if __name__ == "__main__":
    main()
