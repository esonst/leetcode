class Solution:
    class LinkNode:
        class Node:
            def __int__(self,val,nextNode=None):
                self.val=val
                self.nextNode=nextNode
        def __init__(self,n):
            self.link=[]*n
        def add(self,rear,head):

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        bin=[1]*numCourses
        for i in range(len(prerequisites)):
            bin[prerequisites[i][1]]-=1;
        queue=[]
