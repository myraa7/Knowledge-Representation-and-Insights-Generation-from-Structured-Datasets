<script>
    import { onMount } from "svelte";

    let htmlcontent = ""
    onMount(async()=>{
        const response =  await fetch('/Insights_and_knowledge.html')
        htmlcontent = await response.text()
    })
</script>
<main>
    <div class="m-4 mr-48 ml-48 h-96 bg-[#a1a19c] overflow-auto p-4">
        {@html htmlcontent}
    </div>
</main>