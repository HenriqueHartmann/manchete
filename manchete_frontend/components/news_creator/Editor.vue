<template>
  <div>
    <div class="p5">
      <div v-if="editor" class="editor">
        <NewsCreatorEditorMenu class="editor_header" :editor="editor" />
        <editor-content
          :editor="editor"
          class="editor_content text-left p-1 border-0"
        />
      </div>
    </div>
  </div>
</template>

<script>
import History from "@tiptap/extension-history";
import Highlight from "@tiptap/extension-highlight";
import StarterKit from "@tiptap/starter-kit";
import { Editor, EditorContent } from "@tiptap/vue-3";

export default {
  components: {
    EditorContent,
  },

  data() {
    return {
      editor: null,
      // content: "",
    };
  },

  mounted() {
    this.editor = new Editor({
      extensions: [
        StarterKit.configure({ history: false, heading: { levels: [1, 2] } }),
        Highlight,
        History,
      ],
      content: '',
      onUpdate: () => {
        // HTML
        // this.$emit("update:modelValue", this.editor.getHTML());
        console.log(this.editor.getHTML())
        
        this.$emit('updateBody', this.editor.getHTML())
        // JSON
        // this.$emit('update:modelValue', this.editor.getJSON())
      },
    });
  },

  beforeDestroy() {
    this.editor.destroy();
  },
};
</script>

<style lang="scss">
.editor {
  background-color: #fff;
  border: 3px solid #0d0d0d;
  border-radius: 0.75rem;
  color: #0d0d0d;
  display: flex;
  flex-direction: column;
  max-height: 26rem;

  &_header {
    align-items: center;
    background: #0d0d0d;
    border-bottom: 3px solid #0d0d0d;
    border-top-left-radius: 0.25rem;
    border-top-right-radius: 0.25rem;
    display: flex;
    flex: 0 0 auto;
    flex-wrap: wrap;
    padding: 0.25rem;
  }

  &_content {
    flex: 1 1 auto;
    overflow-x: hidden;
    overflow-y: auto;
    padding: 1.25rem 1rem;
    -webkit-overflow-scrolling: touch;
    &::-webkit-scrollbar-track {
      -webkit-box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.3) !important;
      background-color: #f5f5f5;
    }
  }
}

.ProseMirror {
  &:focus {
    border: 0 !important;
    outline: none !important;
  }

  > * + * {
    margin-top: 0.75em;
  }

  blockquote {
    padding-left: 1rem;
    border-left: 3px solid rgba(#0d0d0d, 0.1);
  }

  ul,
  ol {
    padding: 0 1rem !important;
  }
  ul {
    display: block;
    list-style-type: disc;
    margin-block-start: 1rem;
    margin-block-end: 1rem;
    margin-inline-start: 0px;
    margin-inline-end: 0px;
    padding-inline-start: 40px;
  }

  ol {
    display: block;
    list-style-type: decimal;
    margin-block-start: 1em;
    margin-block-end: 1em;
    margin-inline-start: 0px;
    margin-inline-end: 40px;
  }

  h1,
  h2,
  h3,
  h4,
  h5,
  h6 {
    line-height: 1.1;
  }

  p {
    display: block;
    margin-block-start: 1em;
    margin-block-end: 1em;
    margin-inline-start: 0px;
    margin-inline-end: 0px;
    font-size: 16px;
  }

  h1 {
    display: block;
    font-size: 2em;
    margin-block-start: 0.67em;
    margin-block-end: 0.67em;
    margin-inline-start: 0px;
    margin-inline-end: 0px;
    font-weight: bold;
  }

  h2 {
    display: block;
    font-size: 1.5em;
    margin-block-start: 0.83em;
    margin-block-end: 0.83em;
    margin-inline-start: 0px;
    margin-inline-end: 0px;
    font-weight: bold;
  }
}
</style>