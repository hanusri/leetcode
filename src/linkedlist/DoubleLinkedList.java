package linkedlist;

public class DoubleLinkedList {
    private Node head, tail;
    private int size;

    private class Node {
        int data;
        Node next, prev;

        public Node(int data, Node next, Node prev) {
            this.data = data;
            this.next = next;
            this.prev = prev;
        }
    }

    public Boolean isEmpty() {
        return size == 0;
    }

    // Empty this linked list, O(n)
    public void clear() {
        Node trav = head;
        while (trav != null) {
            Node next = trav.next;
            trav.prev = trav.next = null;
            trav = next;
        }
        head = tail = trav = null;
        size = 0;
    }

    // Return the size of this linked list
    public int size() {
        return size;
    }

    public void addFirst(int data) {
        if (isEmpty()) {
            head = tail = new Node(data, null, null);
        } else {
            head.prev = new Node(data, head, null);
            head = head.prev;
        }
        size++;
    }

    public void addLast(int data) {
        if (isEmpty()) {
            head = tail = new Node(data, null, null);
        } else {
            tail.next = new Node(data, null, tail);
            tail = tail.next;
        }
        size++;
    }

    public void addAt(int index, int data) throws Exception {
        if (index < 0 || index > size) {
            throw new Exception("Illegal Index");
        }
        if (index == 0) {
            addFirst(data);
            return;
        }
        if (index == size) {
            addLast(data);
            return;
        }
        Node temp = head;
        for (int i = 0; i < index - 1; i++) {
            temp = temp.next;
        }
        Node newNode = new Node(data, temp.next, temp);
        temp.next = newNode;
        newNode.next.prev = newNode;
        size++;
    }

    public int removeFirst() {
        // Can't remove data from an empty list
        if (isEmpty()) throw new RuntimeException("Empty list");
        int data = head.data;
        head = head.next;
        size--;
        if (isEmpty()) tail = null;
        else head.prev = null;
        return data;
    }

    public int removeLast() {
        // Can't remove data from an empty list
        if (isEmpty()) throw new RuntimeException("Empty list");
        int data = tail.data;
        tail = tail.prev;
        size--;
        if (isEmpty()) head = null;
        else tail.next = null;
        return data;
    }

    public Boolean remove(int data) {
        Node trav = head;
        for (; trav != null; trav = trav.next) {
            if (trav.data == data) {
                remove(trav);
                return true;
            }
        }
        return false;
    }

    public void removeAt(int index) {
        // Make sure the index provided is valid
        if (index < 0 || index >= size) {
            throw new IllegalArgumentException();
        }

        int i;
        Node trav;

        if (index < size / 2) {
            for (i = 0, trav = head; i != index; i++) {
                trav = trav.next;
            }
        } else {
            for (i = size - 1, trav = tail; i != index; i--) {
                trav = trav.prev;
            }
        }
        remove(trav);
    }

    private void remove(Node node) {
        // If the node to remove is somewhere either at the
        // head or the tail handle those independently
        if (node.prev == null) {
            removeFirst();
            return;
        }
        if (node.next == null) {
            removeLast();
            return;
        }

        node.prev.next = node.next;
        node.next.prev = node.prev;

        node.next = node.prev = null;
    }

    public int indexOf(int data) {
        int index = 0;
        for (Node trav = head; trav != null; trav = trav.next, index++) {
            if (trav.data == data) {
                return index;
            }
        }
        return -1;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("[ ");
        Node trav = head;
        while (trav != null) {
            sb.append(trav.data);
            if (trav.next != null) {
                sb.append(", ");
            }
            trav = trav.next;
        }
        sb.append(" ]");
        return sb.toString();
    }

    public static void main(String[] args) {
        DoubleLinkedList list = new DoubleLinkedList();
        list.addLast(5);
        list.addFirst(2);
        list.addLast(6);
        System.out.println(list);
        list.addLast(10);
        System.out.println(list);
        list.remove(6);
        System.out.println(list);
    }

}
