# Grand-Library---Python-Practice
The **Grand Library** project is a Python-based application that simulates a complete library management system. It allows users to manage library items such as books and magazines, including attributes like title, author, genre, pages, issue numbers, and availability. Users can borrow and return items, with different borrowing limits for normal and premium users. The project emphasizes object-oriented programming concepts including abstraction, encapsulation, inheritance, and polymorphism, while also implementing aggregation to manage collections of items and users. It features a menu-driven interface using loops and conditionals, file persistence via JSON to save and load library data, and a testing suite to ensure reliability.

- Concepts to cover are as follows:
  - [ ] **Abstract Base Classes (Abstraction)** – Core structure defined with abstract methods.
  - [ ] **Polymorphism** – Subclasses override methods for custom behavior.
  - [ ] **Encapsulation** – Private attributes with controlled access.
  - [ ] **Inheritance** – User base class extended by NormalUser and PremiumUser.
  - [ ] **Aggregation** – Library contains Items and Users.
  - [ ] **Control Flow** – Loops and conditionals in the main menu for user interaction.
  - [ ] **Persistence** – Save and load state using JSON.
  - [ ] **Testing Suite** – Unit tests for books, users, and library functionality.
  - [ ] **Development Workflow** – Git version control with documentation support.

## UML Class Diagram

```text
                ┌────────────────────────┐
                │     LibraryItem (ABC)  │
                │────────────────────────│
                │ - id: int              │
                │ - title: str           │
                │ - author: str          │
                │ - genre: str           │
                │ - price: float         │
                │ - available: bool      │
                │────────────────────────│
                │ + get_info(): str      │ (abstract)
                │ + borrow(): None       │ (abstract)
                │ + return_item(): None  │ (abstract)
                └───────────▲────────────┘
                            │
          ┌─────────────────┴───────────────────┐
          │                                     │
┌──────────────────────────┐      ┌───────────────────────────┐
│        Book              │      │        Magazine           │
│──────────────────────────│      │───────────────────────────│
│ - pages: int             │      │ - issue_number: int       │
│──────────────────────────│      │───────────────────────────│
│ + get_info(): str        │      │ + get_info(): str         │
│ + borrow(): None         │      │ + borrow(): None          │
│ + return_item(): None    │      │ + return_item(): None     │
└──────────────────────────┘      └───────────────────────────┘


┌──────────────────────────┐
│         User             │
│──────────────────────────│
│ - id: int                │
│ - name: str              │
│ - borrowed_items: list   │
│──────────────────────────│
│ + borrow_item(item)      │
│ + return_item(item)      │
│ + can_borrow(): bool     │ (polymorphic)
└───────────▲──────────────┘
            │
   ┌────────┴─────────┐
   │                  │
┌──────────────────┐  ┌─────────────────────┐
│ NormalUser       │  │ PremiumUser         │
│──────────────────│  │─────────────────────│
│ (max 3 items)    │  │ (max 10 items)      │
│──────────────────│  │─────────────────────│
│ + can_borrow()   │  │ + can_borrow()      │
└──────────────────┘  └─────────────────────┘


┌──────────────────────────┐
│        Library           │
│──────────────────────────│
│ - name: str              │
│ - collection: list       │ (aggregates LibraryItems)
│ - users: list            │
│──────────────────────────│
│ + add_item(item)         │
│ + remove_item(id)        │
│ + search(title)          │
│ + save_to_json(file)     │
│ + load_from_json(file)   │
└──────────────────────────┘