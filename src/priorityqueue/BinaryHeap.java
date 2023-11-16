package priorityqueue;

public class BinaryHeap {
    private static final int DEFAULT_CAPACITY = 100;
    private Integer[] array;

    private int currentSize;

    public BinaryHeap() {
        this(DEFAULT_CAPACITY);
    }

    public BinaryHeap(int capacity) {
        currentSize = 0;
        array = new Integer[capacity + 1];
    }

    public Integer findMin() {
        if (currentSize == 0) {
            return null;
        }

        return array[1];
    }

    public Boolean isEmpty() {
        return currentSize == 0;
    }

    public Boolean isFull() {
        return currentSize == array.length - 1;
    }

    public void insert(int value) throws Exception {
        if (isFull()) {
            throw new Exception("Queue is out of capacity");
        }

        int hole = ++currentSize;
        for (; hole > 1 && value < array[hole / 2]; hole = hole / 2)
            array[hole] = array[hole / 2];
        array[hole] = value;
    }

    public Integer deleteMin() throws Exception {
        if (isEmpty()) {
            throw new Exception("Queue is empty");
        }

        Integer result = findMin();
        array[1] = array[currentSize--];
        percolateDown(1);
        return result;
    }

    private void percolateDown(int hole) {
        int value = array[hole];
        int child;
        for (; hole * 2 <= currentSize; hole = child) {
            child = hole * 2;
            if (child != currentSize && array[child + 1] < array[child])
                child = child + 1;
            if (array[hole] > array[child]) {
                array[hole] = array[child];
            } else {
                break;
            }
        }
        array[hole] = value;
    }

    private void buildHeap() {
        for (int i = currentSize / 2; i > 0; i--)
            percolateDown(i);
    }

    public static void main( String [ ] args )
    {
        int numItems = 10000;
        BinaryHeap h = new BinaryHeap( numItems );
        int i = 37;

        try
        {
            h.insert(15);
            h.insert(4);
            h.insert(98);
            h.insert(12);
            h.insert(8);
            h.insert(26);
            System.out.println( "Min value is " + h.findMin());
            System.out.println( "Deleting the min value is " + h.deleteMin());
            System.out.println( "Min value is " + h.findMin());
            h.insert(2);
            System.out.println( "Min value is " + h.findMin());
        }
        catch( Exception e )
        { System.out.println( "Overflow (expected)! " + i  ); }
    }
}
