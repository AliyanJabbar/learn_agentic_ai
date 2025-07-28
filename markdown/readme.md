# Markdown Examples and Syntax Guide

---

## 🟦 Headings

# Heading 1

<!-- There should be a space between hashtag (#) and the heading -->

#Heading ← (❌ Won’t render properly — missing space)

##### Heading level 5

HTML equivalent:

```html
<h1>Heading 1</h1>
```

---

## 🟦 Paragraphs

**HTML:**

```html
<p>This is the first line. And this is the second line.</p>
```

**Markdown:**

This is the first line. And this is the second line.

👉 If you want to start your paragraph with an empty space, don’t use space or tab. Instead, use `&nbsp;`

---

## 🟦 Line Breaks

**HTML:**

```html
<p>
  This is the first line.<br />
  And this is the second line.
</p>
```

**Markdown (add two spaces at the end of the line):**

This is the first line.  
And this is the second line.

---

## 🟦 Bold Text

Markdown:

```md
**bold text**
**bold text**
```

Rendered Output:  
**bold text**

---

## 🟦 Italic Text

Markdown:

```md
_italic_
_italic_
```

Rendered Output:  
_italic_

---

## 🟦 Bold + Italic

```md
**_bold & italic_**
**_bold & italic_**
```

Rendered Output:  
**_bold & italic_**

---

## 🟦 Blockquotes

```md
> Dorothy followed her through many of the beautiful rooms in her castle.
```

Rendered Output:

> Dorothy followed her through many of the beautiful rooms in her castle.

---

## 🟦 Blockquotes with Other Elements

```md
> #### The quarterly results look great!
>
> - Revenue was off the chart.
> - Profits were higher than ever.
>
>   _Everything_ is going according to **plan**.
```

Rendered Output:

> #### The quarterly results look great!
>
> - Revenue was off the chart.
> - Profits were higher than ever.
>
>   _Everything_ is going according to **plan**.

---

## 🟦 Ordered Lists

```md
1. I am Aliyan
2. My friend Awais
```

Rendered Output:

1. I am Aliyan
2. My friend Awais

---

## 🟦 Unordered Lists

```md
- Aliyan
- Awais
```

Rendered Output:

- Aliyan
- Awais

---

## 🟦 Starting Unordered List with Numbers

```md
- 1968\. A great year!
```

Rendered Output:

- 1968. A great year!

---

## 🟦 Paragraph Inside a List Item

```md
- First item

  This is a new paragraph inside the list.
```

---

## 🟦 Inline Code

```md
Use the `cd` command to change directory.
```

```md
`` Use `code` in Markdown. ``
```

Rendered Output:  
Use the `cd` command to change directory.  
`` Use `code` in Markdown. ``

---

## 🟦 Code Blocks

### ✅ JavaScript Example

```js
function greet() {
  console.log("Hello");
}
```

### ✅ Python Example

```python
def greet():
  print("Hello")
```

### ✅ HTML (Indented with 4 spaces)

```md
    <html>
      <head>
      </head>
    </html>
```

⚠️ **This won't work without indenting:**

```html
<html>
  <head> </head>
</html>
```

---

## 🟦 Horizontal Lines

### In Markdown:

```md
---
---

---
```

---

### In HTML:

```html
<hr />
```

---

## 🟦 Links

```md
[Duck Duck Go](https://duckduckgo.com)

[my portfolio](https://aliyan-jabbar-portfolio.vercel.app)
```

**Rendered Output:**

[Duck Duck Go](https://duckduckgo.com)

[my portfolio](https://aliyan-jabbar-portfolio.vercel.app)

---

## 🟦 Tooltip in Links

### Example 1 (Reference-style):

```md
[var]: https://aliyan-jabbar-portfolio.vercel.app "PORTFOLIO"

[my portfolio][var]
```

**Rendered Output:**

[var]: https://aliyan-jabbar-portfolio.vercel.app "PORTFOLIO"

[my portfolio][var]

### Example 2 (Inline):

```md
My favorite search engine is [Duck Duck Go](https://duckduckgo.com "The best search engine for privacy").
```

**Rendered Output:**

My favorite search engine is [Duck Duck Go](https://duckduckgo.com "The best search engine for privacy").

---

## 🟦 Escaping Special Characters

To prevent Markdown from formatting special characters, use a backslash (`\`):

```md
\* This is not a bullet point
```

Rendered Output:  
\* This is not a bullet point

---

✅ You can now copy and paste this entire markdown into a `.md` file and it will render correctly in any Markdown viewer like VS Code, GitHub, or markdown preview extensions.

---

## 🟦 Images

Here’s a real image example using a landscape from Unsplash:

```md
![Beautiful Landscape](https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=800&q=80 "Nature")
```

**Rendered Output:**


![Beautiful Landscape](https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=800&q=80 "Nature")