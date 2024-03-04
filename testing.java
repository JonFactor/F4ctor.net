class Solution {
    public static void main(String []args)
    {
        String[] list = {"flower","flow","flight"};
        System.out.println(longestCommonPrefix(list));
    }

 public static String longestCommonPrefix(String[] strs) {
    if (strs.length == 0) return "";
    String prefix = strs[0];
    for (int i = 1; i < strs.length; i++)
        while (strs[i].indexOf(prefix) != 0) {
            prefix = prefix.substring(0, prefix.length() - 1);
            if (prefix.isEmpty()) return "";
        }        
    return prefix;
    }
}