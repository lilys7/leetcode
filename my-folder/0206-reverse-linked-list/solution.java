/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode newList = new ListNode();
        ListNode newListCurr = newList;
        ListNode curr = head;
        ArrayList<Integer> arr = new ArrayList<>();
        while (curr != null) {
            arr.add(curr.val);
            curr = curr.next;
        }

        for (int i = arr.size()-1; i >= 0; i--){
            newListCurr.next = new ListNode(arr.get(i));
            newListCurr = newListCurr.next;
        }
        return newList.next;
    }
}
