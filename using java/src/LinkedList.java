class LinkedList{
	Node head;
	static class Node{
		int data;
		Node next;
		Node(int d){
			data = d;
			next = null;
		}
	}

	public static LinkedList insertAtBeg(LinkedList list,int data){
		Node newNode = new Node(data);
		if(list.head == null){
			list.head = newNode;
		}
		else{
			newNode.next = list.head;
			list.head = newNode;
		}
		return list;
	}

	public static LinkedList insert(LinkedList list,int data){
		Node newNode = new Node(data);
		if(list.head == null){
			list.head = newNode;
		}
		else{
			Node currentNode = list.head;
			while(currentNode.next != null){
				currentNode = currentNode.next;
			}
			currentNode.next = newNode;

		}
	return list;

	}


	public static LinkedList insertAtIndex(LinkedList list,int data, int index){
		Node newNode = new Node(data);
		if(index == 0){
			insertAtBeg(list, data);
		}
		else{
			Node currentNode = list.head;
			while(index-- != 0){
				if(index == 0){
					newNode.next = currentNode.next;
					currentNode.next = newNode;
					break;
				}
				currentNode = currentNode.next;
			}
			if(index !=0){
				System.out.println("Index not found");
			}
		}
		return list;

	}

	public static LinkedList deleteNode(LinkedList list,int data){

		Node currentNode = list.head,prev = null;
		if(currentNode!=null && currentNode.data == data){
			list.head = currentNode.next;
			return list;
		}
		while(currentNode!=null && currentNode.data!=data){
			prev = currentNode;
			currentNode = currentNode.next;
		}
		if(currentNode!=null){
			prev.next = currentNode.next;
			return list;
		}
		if(currentNode == null){
			System.out.println("Data does not exist.");
		}

	return list;		
	}


	public static void printList(LinkedList list)
    {
        Node currNode = list.head;
    
        System.out.print("LinkedList: ");
    
        while (currNode != null) {
            System.out.print(currNode.data + " ");
            currNode = currNode.next;
        }
	}
	public static void main(String[] args) {
		LinkedList list = new LinkedList();
		list = insert(list, 1);
		list = insert(list,2);
		list = insert(list,4);
		list = insertAtBeg(list, 0);
		list = insertAtIndex(list, 3, 3);
		printList(list);
		System.out.println();
		list = deleteNode(list, 2);
		printList(list);
	}


}