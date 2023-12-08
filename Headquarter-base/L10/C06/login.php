<?php
$key = '';
extract($_GET);
if ($key !== $password) {
?>
  <div class="main">
    <div class="logo"><img src="../assets/images/challenge-chirp-logo.svg" alt="Chirp logo"></div>

    <form class="form" method="GET">
      <div class="message message-error" id="msg-incorrect" style="display: none">Wrong. No chirping today.</div>

      <div class="field">
        <div class="label">Username</div>

        <input type="text" name="username" id="username">
      </div>

      <div class="field">
        <div class="label">Password</div>

        <input type="password" name="password" id="password">
      </div>

      <div class="actions">
        <input type="submit" value="Enter" class="btn">
      </div>
    </form>
  </div>
<?php
} else {
    require_once("emails");
};
?>
