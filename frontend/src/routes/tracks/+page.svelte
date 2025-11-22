<script lang="ts">
  import { onMount } from 'svelte';

  const API_BASE = 'http://127.0.0.1:8000';

  type Track = {
    id: string;
    song_name: string;
    artist: string;
    duration: string;
  };

  let tracks: Track[] = [];
  let loading = true;
  let error: string | null = null;

  async function loadTracks() {
    loading = true;
    error = null;

    try {
      const res = await fetch(`${API_BASE}/tracks`);
      if (!res.ok) {
        throw new Error(`Failed to load tracks (${res.status})`);
      }
      tracks = await res.json();
    } catch (err) {
      error = err instanceof Error ? err.message : 'Unknown error';
    } finally {
      loading = false;
    }
  }

  onMount(loadTracks);
</script>

<main>
  <h1>Available Songs!</h1>

  <section class="mt-4">
    <h2 class="mb-3">Tracks</h2>

    {#if tracks.length === 0}
      <p class="text-muted">No tracks yet.</p>
    {:else}
      <div class="track-list">
        {#each tracks as t}
          <div class="track-item d-flex align-items-center justify-content-between">
            <div class="d-flex align-items-center">
              <div class="track-avatar me-3 d-flex align-items-center justify-content-center">
                <i class="bi bi-music-note-beamed"></i>
              </div>

              <div>
                <a href={`/tracks/${t.id}`} class="fw-semibold text-decoration-none">
                  {t.song_name}
                </a>
                <div class="text-muted small">{t.artist}</div>
              </div>
            </div>

            <div class="d-flex align-items-center gap-3">
              <span class="text-muted small">{t.duration}</span>
        
               </div>
          </div>
        {/each}
      </div>
    {/if}
  </section>
</main>

<style>
  .track-list {
    border-top: 1px solid #eee;
    margin-top: 0.5rem;
  }

  .track-item {
    padding: 0.75rem 0;
    border-bottom: 1px solid #f1f1f1;
    transition: background 0.15s ease, transform 0.1s ease;
  }

  .track-item:hover {
    background: #f8fafc;
    transform: translateY(-1px);
  }

  .track-avatar {
    width: 40px;
    height: 40px;
    border-radius: 999px;
    background: #111827;
    color: white;
    font-size: 1.1rem;
  }

  .track-avatar i {
    display: block;
  }
</style>

