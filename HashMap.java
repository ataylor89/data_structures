import java.util.List;
import java.util.ArrayList;

/**
 * This is an implementation of a hash map in Java.
 * It uses a hash table and buckets consisting of linked lists.
 * The hash function simply performs the mod operator on the key's hash code.
 * This implementation supports the put, get, remove, and toString operations.
 */
public class HashMap<K,V> {
    
    private class HashNode<K,V> {
        K key;
        V value;
        HashNode<K,V> next;

        HashNode(K key, V value) {
            this.key = key;     
            this.value = value;
        }
    }

    private List<HashNode<K,V>> hashTable;
    private int capacity;   
    private int size;

    public HashMap(int capacity) {
        this.hashTable = new ArrayList<>(capacity);
        this.capacity = capacity;

        for (int i = 0; i < capacity; i++)
            hashTable.add(i, null);
    }

    public void put(K key, V value) {
        int hashIndex = hash(key);

        HashNode<K,V> insertion = new HashNode<>(key, value);

        if (hashTable.get(hashIndex) == null) {
            hashTable.add(hashIndex, insertion);
            size++;
        }

        else {
            HashNode<K,V> entry = hashTable.get(hashIndex);
            HashNode<K,V> prev = null;        

            while (entry != null && entry.key != key) { 
                prev = entry;
                entry = entry.next;
            }

            if (entry != null) // entry must have matching key, so replace this key's value with the new one 
                entry.value = value;            
            
            else { // the key was not found at this hash index, so add it to the linked list
                prev.next = insertion;
                size++;
            } 
        }
    }

    public V get(K key) {
        int hashIndex = hash(key);

        HashNode<K,V> entry = hashTable.get(hashIndex);
        
        while (entry != null && entry.key != key) 
            entry = entry.next;
    
        return entry == null ? null : entry.value;
    }

    public void remove(K key) {
        int hashIndex = hash(key);

        HashNode<K,V> entry = hashTable.get(hashIndex);

        if (entry == null)
            return;

        HashNode<K,V> prev = null;

        while (entry != null && entry.key != key) {
            prev = entry;
            entry = entry.next;
        }
     
        if (prev == null) { // there's one node in the bucket and it has a matching key
            hashTable.set(hashIndex, null);
            size--;
        }
        
        else if (entry != null) { // more than one node in the bucket, and entry has a matching key
            prev.next = entry.next;
            size--;
        }
    }

    private int hash(K key) {
        int hc = key.hashCode();
        hc = (hc >= 0) ? hc : hc * -1;
        return hc % capacity;
    }

    @Override
    public String toString() {
        StringBuilder s = new StringBuilder();
        s.append("{");
        int count = 0;
        for (int i = 0; i < hashTable.size(); i++) {
            if (hashTable.get(i) == null)   
                continue;            

            s.append("\"" + hashTable.get(i).key + "\"");
            s.append(": ");
            s.append("\"" + hashTable.get(i).value + "\"");

            if (count < size - 1)
                s.append(", ");

            count++;
        }
        s.append("}");
        return s.toString();
    }

    public static void main(String[] args) {
        HashMap<String, String> map = new HashMap<>(50);

        System.out.println("Putting breakfast, lunch and dinner into the map...");
        map.put("Breakfast", "Coffee and eggs");
        map.put("Lunch", "Tuna sandwich and beans");
        map.put("Dinner", "Pasta and vegetables");

        System.out.println("Breakfast: " + map.get("Breakfast"));
        System.out.println("Lunch: " + map.get("Lunch"));
        System.out.println("Dinner: " + map.get("Dinner"));

        System.out.println("Removing lunch...");
        map.remove("Lunch");
        
        System.out.println("Adding dessert and tea");
        map.put("Dessert", "Ice cream");
        map.put("Tea", "Chamomile");

        System.out.println("Displaying map...");
        System.out.println(map);
    }
}
