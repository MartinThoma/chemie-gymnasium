---
layout: post
title: Kontakt
summary: 
slug: kontakt
author: Martin Thoma
date: 2008-09-07T19:49:27
category: 
featured_image: 
---
<h1>Kontakt</h1>
<form method="post" action="send_email.php" class="kontakt" name="feedback">
<fieldset>
  <legend>Kontaktformular</legend>
    <label for="grund">Kontaktgrund</label>
<select id="grund" name="grund">
    <option>Rechtschreibfehler / Inhaltsfehler</option>
    <option>Verbesserungsvorschlag</option>
    <option>Sonstiges</option>
</select>
    <label for="betreff">Betreff</label><input id="betreff" name="betreff" type="text" />
    <label for="email">Email</label><input id="email" name="email" type="text"  class="required validate-email"/>
    <textarea name="text" rows="30" cols="20"></textarea>
    <input type="submit" value="Abschicken" />
</fieldset>
</form>
<script type="text/javascript">
   new Validation('feedback', {immediate:true});
</script>
