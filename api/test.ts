export async function GET() {
  return Response.json({
    message: 'Hello from Vercel Bun API!',
    bun: process.versions.bun ?? null,
    node: process.versions.node ?? null,
  });
}

export async function POST(request: Request) {
  const body = await request.json();
  return Response.json({ received: body, timestamp: Date.now() });
}
