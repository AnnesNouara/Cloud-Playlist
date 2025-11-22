<script lang="ts">
  import { onMount } from 'svelte';
  import { page } from '$app/stores';
	import { goto } from '$app/navigation';

  const API_BASE = 'http://127.0.0.1:8000';

  type Track = {
    id: number;
    song_name: string;
    artist: string;
    duration: string;
  };

  let id: string | undefined;
  $: id = $page.params.id;

  let track: Track | null = null;
  let loading = true;
  let error: string | null = null;

  let song_name = '';
  let artist = '';
  let duration = '';

  onMount(loadTrack);

  async function loadTrack() {
    error = null;
    loading = true;

    try {
      const res = await fetch(`${API_BASE}/tracks/${id}`);

      if (!res.ok) {
        throw new Error(`Failed to load track (${res.status})`);
      }

      const data: Track = await res.json();
      track = data;

      song_name = track.song_name;
      artist = track.artist;
      duration = track.duration;

    } catch (err) {
      error = err instanceof Error ? err.message : "Unknown error";
    } finally {
      loading = false;
    }
  }

  async function editTrack() {
    if (!id) return;
    error = null;

    try {
      const res = await fetch(`${API_BASE}/tracks/${id}/edit`, {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ song_name, artist, duration })
      });

      if (!res.ok) throw new Error(`Failed to update track (${res.status})`);

      const updated: Track = await res.json();
      track = updated;
      alert('Track has been updated')
      goto('/tracks')

    } catch (err) {
      error = err instanceof Error ? err.message : "Unknown error";
    }
  }
</script>

<main class="container">
  <h1>Cloud Playlist Tracker</h1>

  {#if loading}
    <p>Loading...</p>
  {:else if error}
    <p class="error">{error}</p>
  {:else if track}
  
    <h2>Edit Track</h2>
    <p class="current-info">
      Editing <strong>{track.song_name}</strong> by <strong>{track.artist}</strong>
    </p>

    <div class="card">
      <form on:submit|preventDefault={editTrack}>
        
        <label>Song name</label>
        <input bind:value={song_name} />

        <label>Artist</label>
        <input bind:value={artist} />

        <label>Duration</label>
        <input placeholder="e.g. 3M 12S" bind:value={duration} />

        <button type="submit">Save Changes</button>
      </form>
    </div>
  {/if}
</main>

<style>
  .container {
    max-width: 550px;
    margin: 0 auto;
    padding: 2rem;
  }

  h1 {
    font-size: 2.3rem;
    margin-bottom: 1.5rem;
  }

  h2 {
    margin: 0 0 0.5rem 0;
    font-size: 1.6rem;
  }

  .current-info {
    margin-bottom: 1rem;
    color: #444;
  }

  .card {
    background: white;
    padding: 1.5rem;
    border-radius: 10px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.08);
  }

  form {
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }

  label {
    font-size: 0.95rem;
    font-weight: 500;
  }

  input {
    padding: 0.7rem;
    border-radius: 6px;
    border: 1px solid #ccc;
    font-size: 1rem;
  }

  button {
    background: #2f5bea;
    color: white;
    padding: 0.8rem;
    border-radius: 6px;
    border: none;
    cursor: pointer;
    font-size: 1rem;
    font-weight: 500;
    margin-top: 0.5rem;
  }

  button:hover {
    background: #1f46c8;
  }

  .error {
    color: #b91c1c;
    background: #fee2e2;
    padding: 0.8rem;
    border-radius: 6px;
    margin-bottom: 1rem;
  }
</style>
