---
title: Guidelines
description: A list of Guidelines
---

# Guidelines

There are important considerations to take into account when defining and planning your cloud-based project. 
Here, we look at some useful guidelines to follow when executing your project.

 - [Tagging Guidelines](tagging)
 - [Security Guidelines](security)
 - [Compliance Guidelines](compliance)


<div class="section-index">
    <hr class="panel-line">
    {% for post in site.docs.guidelines  %}        
    <div class="entry">
    <h5><a href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a></h5>
    <p>{{ post.description }}</p>
    </div>{% endfor %}
</div>