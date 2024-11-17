<template>
  <div class="min-h-screen flex flex-col justify-start items-center text-white animated-bg relative">
    <!-- Decorative sides -->
    <div class="side-design left-side absolute top-0 left-0 h-full w-16 md:w-32"></div>
    <div class="side-design right-side absolute top-0 right-0 h-full w-16 md:w-32"></div>

    <!-- Centered AKA logo and title -->
    <div class="flex flex-col items-center z-10 mt-16"> <!-- Adjusted margin for higher position -->
      <!-- AKA Logo -->
      <div class="logo-container transform -rotate-180 mb-4 text-center">
        <span class="text-7xl font-unifrakturcook">AKA</span>
      </div>
      <!-- Lexicon Lookup Title -->
      <div class="title-container text-center mb-6">
        <h1 class="text-3xl font-late1800s">Lexicon Lookup</h1>
      </div>
      <!-- Search Bar -->
      <div class="search-bar flex items-center w-full max-w-md p-2 border border-gray-300 rounded-md bg-white text-black shadow-lg">
        <input
          v-model="searchQuery"
          type="text"
          placeholder="Search..."
          class="flex-grow px-3 py-2 text-sm border-none focus:outline-none"
        />
        <button
          @click="performSearch"
          class="px-4 py-2 ml-2 text-sm font-medium text-white bg-blue-600 rounded-md hover:bg-blue-700 focus:outline-none"
        >
          Search
        </button>
      </div>
    </div>

    <!-- Search results -->
    <div
      v-if="results.length"
      class="results mt-6 w-full max-w-md p-4 bg-white text-black border border-gray-300 rounded-md shadow-lg z-10"
    >
      <ul>
        <li
          v-for="result in results"
          :key="result"
          class="py-2 border-b border-gray-200 last:border-b-0"
        >
          {{ result }}
        </li>
      </ul>
    </div>
  </div>
</template>

<!-- <script setup>
import { ref } from "vue";

const searchQuery = ref("");
const results = ref([]);

const performSearch = () => {
  const lexicon = ["Serendipity", "Quixotic", "Euphoria", "Ineffable"];
  results.value = lexicon.filter((word) =>
    word.toLowerCase().includes(searchQuery.value.toLowerCase())
  );
};
</script> -->

<script setup>
import { ref } from "vue";
import axios from "axios";
import permutations from "just-permutations";

const searchQuery = ref(""); // Reactive variable for search input
const results = ref([]); // Reactive variable for search results
const loading = ref(false); // Reactive variable for loading state

const performSearch = async () => {
  loading.value = true;
  const charArray = searchQuery.value.split("");
  const wordPermutations = [...new Set(permutations(charArray))];
  const validWords = [];
  const words = wordPermutations.map((wordArray) => wordArray.join(""));
  console.log(words);
  for (const word of words) {
    try {
      const response = await axios.get(`http://localhost:8000/dictionary/${word}`);
      if (response.status === 200) {
        validWords.push(word);
      }
    } catch (err) {
      // Ignore 404 errors
    }
  }

  results.value = validWords;
  loading.value = false;
};
</script>


<!--
<template>
  <div id="app">
    <h1 class="text-4xl">LEXICON LOOKUP</h1>
    <input type="text" v-model="characters" placeholder="Enter characters" />
    <button @click="generateWords">Find Words</button>
    <div v-if="loading" class = "text-6xl">Loading...</div>
    <div v-if="words.length">
      <h2>Valid Words</h2>
      <ul>
        <li v-for="word in words" :key="word">{{ word }}</li>
      </ul>
    </div>
  </div>
</template> -->


<style scoped>
body {
  font-family: Arial, sans-serif;
}
#app {
  padding: 20px;
}
</style> */}

<style scoped>
/* Font Definitions */
@font-face {
  font-family: "UnifrakturCook";
  src: url("https://fonts.gstatic.com/s/unifrakturcook/v17/-F61fjF3ITQwasLhLkTZP1pRtqw.woff2") format("woff2");
  font-style: normal;
  font-weight: 400;
}

@font-face {
  font-family: "Uncial Antiqua";
  src: url("https://fonts.gstatic.com/s/uncialantiqua/v17/N0bM2S5WOex4OUbESzoESK-e.woff2") format("woff2");
  font-style: normal;
  font-weight: 400;
}

@font-face {
  font-family: "Great Vibes";
  src: url("https://fonts.gstatic.com/s/greatvibes/v15/RWmMoKWR9v4ksMfaWd_JN9XFiaQ5IQ.woff2") format("woff2");
  font-style: normal;
  font-weight: 400;
}

/* Apply Font Styling */
body {
  font-family: sans-serif;
}

.font-unifrakturcook {
  font-family: "UnifrakturCook", cursive;
}

.font-late1800s {
  font-family: "Great Vibes", cursive;
  font-size: 3rem; /* Adjust size as needed */
  font-weight: 400; /* Light-weight cursive font */
}

/* Gradient Background */
.animated-bg {
  background: linear-gradient(90deg, #ff6a00, #ee0979, #00c9ff, #92fe9d);
  background-size: 400% 400%;
  animation: gradientBG 10s ease infinite;
}

@keyframes gradientBG {
  0% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0% 50%;
  }
}

/* Side Designs */
.side-design {
  background: repeating-linear-gradient(
    45deg,
    rgba(255, 255, 255, 0.1),
    rgba(255, 255, 255, 0.1) 10px,
    rgba(0, 0, 0, 0.05) 10px,
    rgba(0, 0, 0, 0.05) 20px
  );
}

.left-side {
  background-color: rgba(255, 255, 255, 0.05);
  clip-path: polygon(0 0, 100% 0, 80% 100%, 0 100%);
}

.right-side {
  background-color: rgba(255, 255, 255, 0.1);
  clip-path: polygon(20% 0, 100% 0, 100% 100%, 0 100%);
}

/* Search Bar */
.search-bar input {
  flex-grow: 1;
}

/* Search Results */
.results ul li:hover {
  background-color: #f3f4f6;
  color: #1a202c;
}
</style>
