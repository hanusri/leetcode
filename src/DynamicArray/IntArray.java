package DynamicArray;

import java.lang.reflect.Array;
import java.util.Arrays;

public class IntArray implements Iterable<Integer> {
    private final int DEFAULT_CAP = 10;
    private int capacity;
    private int len;

    private int[] arr;
    public IntArray() {
        arr = new int[DEFAULT_CAP];
    }

    public IntArray(int capacity) {
        if (capacity < 0) throw new IllegalArgumentException("Illegal Capacity: " + capacity);
        arr = new int[capacity];
    }

    public IntArray(int[] array) {
        if (array == null) throw new IllegalArgumentException("Array cannot be null");
        arr = Arrays.copyOf(array, array.length);
        len = capacity = arr.length;
    }

    // Returns the size of the array
    public int size() {
        return len;
    }

    // Returns true/false on whether the array is empty
    public boolean isEmpty() {
        return len == 0;
    }

    public int get(int index) {
        return arr[index];
    }

    public void set(int index, int elem) {
        arr[index] = elem;
    }

    public void add(int element) {
        if (len + 1 >= capacity) {
            if (capacity == 0) capacity = 1;
            else capacity *= 2; // double the size
            arr = Arrays.copyOf(arr, capacity); // pads with extra 0/null elements
        }
        arr[len++] = element;
    }

    public void removeAt(int rm_index) {
       if(rm_index >= len || rm_index < 0) {
           throw new IllegalArgumentException("Remove index is out of range");
       }
       int[] new_arr = new int[len - 1];
       for(int i=0, j = 0; i< len;i++,j++){
           if(i == rm_index) j--;
           else new_arr[j] = arr[i];
       }
       arr = new_arr;
       capacity = --len;
    }

    public boolean remove(int elem) {
        for (int i = 0; i < len; i++) {
            if (arr[i] == elem) {
                removeAt(i);
                return true;
            }
        }
        return false;
    }

    public void reverse() {
        for(int i = 0;i < len / 2;i++){
            int temp = arr[i];
            arr[i] = arr[len - i - 1];
            arr[len - i - 1] = temp;
        }
    }

    @Override
    public java.util.Iterator<Integer> iterator() {
        return new java.util.Iterator<Integer>() {
            int index = 0;

            public boolean hasNext() {
                return index < len;
            }

            public Integer next() {
                return arr[index++];
            }

            public void remove() {
                throw new UnsupportedOperationException();
            }
        };
    }

    @Override
    public String toString() {
        if (len == 0) return "[]";
        else {
            StringBuilder sb = new StringBuilder(len).append("[");
            for (int i = 0; i < len - 1; i++) sb.append(arr[i] + ", ");
            return sb.append(arr[len - 1] + "]").toString();
        }
    }

    // Example usage
    public static void main(String[] args) {

        IntArray ar = new IntArray(50);
        ar.add(3);
        ar.add(7);
        ar.add(6);
        ar.add(-2);
        ar.add(56);
        ar.add(12);
        ar.add(98);

        System.out.println(ar);

        ar.removeAt(3);

        System.out.println(ar);

        ar.reverse();

        System.out.println(ar);
    }

}
