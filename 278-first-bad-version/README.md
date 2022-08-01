<h2><a href="https://leetcode.com/problems/first-bad-version/">278. First Bad Version</a></h2><h3>Easy</h3><hr><div><p>You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. <gistnote class="gistnote-highlight" highlightid="1c083b05-00d4-4c2d-b5ac-f365fb9773cb" colornum="3" style="background-color: rgb(255, 251, 120);" id="1c083b05-00d4-4c2d-b5ac-f365fb9773cb">Since each version is developed based on the previous version, all the versions after a bad version are also bad.</gistnote></p>

<p>Suppose you have <code>n</code> versions <code>[1, 2, ..., n]</code> and you want to find out the first bad one, which causes all the following ones to be bad.</p>

<p>You are given an API <code>bool isBadVersion(version)</code> which returns whether <code>version</code> is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> n = 5, bad = 4
<strong>Output:</strong> 4
<strong>Explanation:</strong>
call isBadVersion(3) -&gt; false
call isBadVersion(5)&nbsp;-&gt; true
call isBadVersion(4)&nbsp;-&gt; true
Then 4 is the first bad version.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> n = 1, bad = 1
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= bad &lt;= n &lt;= 2<sup>31</sup> - 1</code></li>
</ul>
</div>