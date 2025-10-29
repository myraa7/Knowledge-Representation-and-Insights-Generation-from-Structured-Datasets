<script>
  export let name;
  import Papa from "papaparse";
  import { onMount } from "svelte";

  let csvData = [];

  onMount(async () => {
    const response = await fetch("/data.csv");
    const csvText = await response.text();
    Papa.parse(csvText, {
      header: true,
      complete: function (results) {
        csvData = results.data;
      },
    });
  });

  function download() {
    const url = '/titanic.csv';
    const anchor = document.createElement('a');
    anchor.href = url;
    anchor.setAttribute('download', 'titanic.csv');
    anchor.click();
  }
</script>

<section class="bg-[#8b79d9] text-gray-900">
  <div class="container mx-auto p-4">
    <h1 class="text-2xl font-bold mb-4">Knowledge Representation and Data Analysis</h1>
    <h2 class="text-xl font-semibold mb-2">Titanic Survival Prediction</h2>
    <div class="mb-4">
      <button class="bg-blue-500 text-black px-4 py-2 rounded hover bg-[#d1c545]" on:click={download}>Download CSV</button>
    </div>
    <div class="bg-white p-8 rounded-lg shadow-lg">
      <h3 class="text-lg font-semibold mb-2">About the Dataset</h3>
      <p class="mb-2">
        The Titanic dataset is a comprehensive record of the passengers aboard the RMS Titanic, which tragically sank on its maiden voyage in April 1912. This dataset includes various attributes of the passengers, such as their survival status (Survived), passenger class (Pclass), name (Name), sex (Sex), age (Age), number of siblings/spouses aboard (SibSp), number of parents/children aboard (Parch), ticket number (Ticket), fare (Fare), cabin number (Cabin), and port of embarkation (Embarked).
      </p>
      <p>
        It provides crucial insights into the demographics and socio-economic conditions of the passengers, which can be analyzed to understand the factors that influenced survival rates.
      </p>
    </div>
  </div>
</section>
