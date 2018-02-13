## HTML5 and CSS3

### CSS3 Transitions, Transforms, Animation and Filters

**About these pages:** *Notes and code samples from **[Murach's HTML5 and CSS3, 3rd Edition](https://www.murach.com/shop/murachs-html5-and-css3-3rd-edition-detail)**. I have been working through this text and compiling what I feel are the key points and examples from each chapter. I would highly recommend the Murach books, they have an interesting approach (content on the left page, examples on the right page) and provide solid foundations for a wide range of programming and database topics.* 

**Transitions**

- `transition`
- `transition-property`
- `transition-duration`
- `transition-timing-function`
- `transition-delay`

**Example**

    #delay {
      font-size: 14px;
      transition-property: font-size;
      transition-duration: 4s;
      transition-delay: 2s;
    }

    #delay:hover {
      font-size: 36px;
    }

**Transforms**

- `transform`
- `transform-origin`

**Example**

    <img style="transform: rotate(90deg);
                transform-origin: bottom left;" 
         src="https://mdn.mozillademos.org/files/12539/Screen%20Shot%202016-02-16%20at%2015.53.54.png">

**Animations**

- `animation-delay`
- `animation-direction`
- `animation-duration`
- `animation-iteration-count`
- `animation-name`
- `animation-play-state`
- `animation-timing-function`
- `animation-fill-mode`

**Example**

    <!-- html -->
    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Dolor cumque iusto quod esse consectetur. Necessitatibus repellendus nobis quas facere inventore?</p>

    /* css */
    p {
      animation-duration: 3s;
      animation-name: slidein;
    }

    @keyframes slidein {
      from {
        margin-left: 100%;
        width: 300%; 
      }

      to {
        margin-left: 0%;
        width: 100%;
      }
    }

**Filters**

- `<blur`
- `<brightness`
- `<contrast`
- `<drop-shadow`
- `<grayscale`
- `<hue-rotate`
- `<invert`
- `<opacity`
- `<saturate`
- `<sepia`

**Example**

    .mydiv {
      filter: grayscale(50%);
    }

    /* Gray all images by 50% and blur by 10px */
    img {
      filter: grayscale(0.5) blur(10px);
    }

**More information**

- **[Transitions](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Transitions/Using_CSS_transitions)**
- **[Transforms](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Transforms/Using_CSS_transforms)**
- **[Animations](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Animations/Using_CSS_animations)**
- **[Filters](https://developer.mozilla.org/en-US/docs/Web/CSS/filter)**