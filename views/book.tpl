%rebase layout

<div class="left" id="search">
  <div>search: <input type="text" id="search-text" /></div>
    <script type="text/javascript">
      onReturnPressed('#search-text', search);
    </script>
  <div id="search-result"></div>
</div>

<div class="right">

  <FORM action="/book" method="post" id="book-form">
    <div class="field">
      <LABEL for="title">title</LABEL>
      <INPUT type="text" id="title">
    </div>

    <div class="field">
      <LABEL for="author">Author</LABEL>
      <INPUT type="text" id="author">
    </div>

    <div class="field">
      <LABEL for="ISBN">ISBN</LABEL>
      <INPUT type="text" id="ISBN">
    </div>

    <div class="control">
      <input type="submit" value="+" />
      <input type="submit" value="-" />
      <input type="submit" value="OK" class="btn-ok"/>
    </div>

  </FORM>


</div>
