<script>
  import { goto } from "$app/navigation";

  function navigate() {
    goto("/custom");
  }
</script>

<header class="bg-[#a1a19c] py-4">
  <div class="flex items-center justify-between">
    <h1 class="text-[#2E4053] text-3xl font-bold ml-8">
        Intel Unnati project 
    </h1>
    <h2 class="text-[#2f07e0] text-xl font-bold ml-6">
      Knowledge Representation and Insight Generation from structured dataset
  </h2>
    <button on:click={navigate} class="mr-8 p-4 pt-2 pb-2 bg-[#d1c545] rounded-3xl">Enter your custom input</button>
  </div>
</header>
